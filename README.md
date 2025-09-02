# Gesture-Based-Sargam-Player
Using finger movements, the sounds Sa, Re Ga Ma Pa Dha Ni Saa are produced.

With the help from ChatGPT, I built a gesture-controlled music system that plays notes when specific hand movements are detected - all in real time. Here’s a detailed look into what I used and how it works:

🛠 Tools & Libraries Used

• OpenCV -Captures and processes real-time video from the webcam.

• MediaPipe - Detects and tracks both hands with high accuracy, giving me exact coordinates of each hand landmark (fingers, joints, etc.).

• math.hypot() - Calculates the distance between two points (like the tip of my index and thumb) to interpret gestures.

• Pygame - Plays `.wav` files instantly when a gesture matches a note trigger.

• Wavtones.com - A function generator I used to create clean sine-wave `.wav` files for each note (Do, Re, Mi, Fa, So, La, Ti, Do).

⚙️ How It Works

1. Video Feed Capture - OpenCV reads each frame from the webcam in real time.

2. Hand Detection - MediaPipe processes the frame and returns landmark coordinates for both hands.

3. Gesture Calculation - Using `math.hypot`, the program measures distances (for example, between the index finger and thumb tips). Each distance range is mapped to a specific musical note.

4. Sound Playback - Pygame triggers the `.wav` file corresponding to that note, playing the sound instantly without lag.

5. Repeat in Real Time - The process loops for each frame, giving an interactive and musical experience.


To make the experience precise, I didn’t use pre-recorded sounds. Instead, I generated pure frequency tones using https://lnkd.in/g-d76cFq. 
Each `.wav` file corresponds to a note frequency in the C-major scale, making it easier to identify individual notes clearly during testing.
▪︎
▪︎
▪︎
▪︎
▪︎
Inspired by: https://lnkd.in/gbdT3gT4
▪︎
▪︎
hashtag#opencv hashtag#mediapipe hashtag#gesturedetection
