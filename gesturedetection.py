import cv2
import mediapipe as mp
import pygame
import math

# --- Initialize Pygame mixer ---
pygame.mixer.init()
notes = {
    "right": {
        "pinky": pygame.mixer.Sound("do.wav"),     # Do (C4 ~261 Hz)
        "ring": pygame.mixer.Sound("re.wav"),      # Re (D4 ~293 Hz)
        "middle": pygame.mixer.Sound("mi.wav"),    # Mi (E4 ~329 Hz)
        "index": pygame.mixer.Sound("fa.wav"),     # Fa (F4 ~349 Hz)
    },
    "left": {
        "pinky": pygame.mixer.Sound("so.wav"),     # So (G4 ~392 Hz)
        "ring": pygame.mixer.Sound("la.wav"),      # La (A4 ~440 Hz)
        "middle": pygame.mixer.Sound("ti.wav"),    # Ti (B4 ~493 Hz)
        "index": pygame.mixer.Sound("do_high.wav") # High Do (C5 ~523 Hz)
    }
}

# --- Mediapipe hands setup ---
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)

def distance(point1, point2):
    return math.hypot(point2[0]-point1[0], point2[1]-point1[1])

cap = cv2.VideoCapture(0)
threshold = 0.05  # Distance threshold for finger touch

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks, hand_label in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = hand_label.classification[0].label.lower()  # 'left' or 'right'
            lm = hand_landmarks.landmark

            thumb = (lm[mp_hands.HandLandmark.THUMB_TIP].x, lm[mp_hands.HandLandmark.THUMB_TIP].y)
            fingers = {
                "pinky": (lm[mp_hands.HandLandmark.PINKY_TIP].x, lm[mp_hands.HandLandmark.PINKY_TIP].y),
                "ring": (lm[mp_hands.HandLandmark.RING_FINGER_TIP].x, lm[mp_hands.HandLandmark.RING_FINGER_TIP].y),
                "middle": (lm[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x, lm[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y),
                "index": (lm[mp_hands.HandLandmark.INDEX_FINGER_TIP].x, lm[mp_hands.HandLandmark.INDEX_FINGER_TIP].y)
            }

            # Check thumb touching other fingers
            for finger, point in fingers.items():
                if distance(thumb, point) < threshold:
                    if finger in notes[label]:
                        notes[label][finger].play()

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Piano", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
