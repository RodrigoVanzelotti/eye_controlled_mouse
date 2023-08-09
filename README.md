# Eye Controlled Mouse using FaceMesh

**Rodrigo Pires Vanzelotti**

This Python script demonstrates an eye-controlled mouse using the MediaPipe library's FaceMesh model. The program utilizes computer vision to track specific facial landmarks, particularly the position of the eyes, and translates these movements into mouse cursor actions. It employs OpenCV for image processing, MediaPipe for face landmark detection, and PyAutoGUI for controlling the mouse.

## Functionality

The script captures video from the webcam, processes each frame, and identifies the landmarks of the face using the FaceMesh model. It then tracks the movement of the eyes and determines whether the user blinks or opens their mouth to perform corresponding actions.

### Key Components

1. **Webcam Capture**: The script accesses the webcam using OpenCV's `cv2.VideoCapture` and retrieves video frames for processing.

2. **FaceMesh Initialization**: The script initializes the FaceMesh model from the MediaPipe library with the option to refine landmarks. This model is responsible for detecting facial landmarks.

3. **Mouse Control**: The main logic of the script involves using facial landmarks to control the mouse cursor. The program identifies the landmarks associated with the user's eyes and calculates cursor movement based on the position of these landmarks.

4. **Blink Detection**: The script detects blinking by monitoring the vertical distance between the upper and lower landmarks of the eye. If this distance is below a certain threshold, a blink is detected.

5. **Mouth Open Detection**: The script also checks whether the user's mouth is open. If the distance between specific mouth landmarks exceeds a threshold, the script temporarily disables cursor control.

6. **Click Action**: Additionally, the script detects when the user's eyes are close enough (vertical distance between eye landmarks below a certain threshold) and simulates a mouse click using `pyautogui.click()`.

7. **Screen Resolution**: The script retrieves the screen's dimensions using `pyautogui.size()` to convert normalized landmark coordinates into actual screen positions.

## FaceMesh and Real-World Applications

**MediaPipe's FaceMesh** is a powerful model for facial landmark detection. It identifies 468 facial landmarks, including eyes, nose, mouth, and other facial features. These landmarks provide valuable information about facial expressions, head orientation, and gaze direction.

**Applications in the Real World**:

1. **Gaze Tracking**: FaceMesh's accurate landmark detection can be used to track a person's gaze direction, enabling applications like gaze-controlled user interfaces, video games, and virtual reality systems.

2. **Emotion Recognition**: By analyzing changes in facial landmarks, FaceMesh can be used to detect emotions such as smiles, frowns, and raised eyebrows. This has applications in sentiment analysis and user engagement evaluation.

3. **Accessibility Tools**: Eye-controlled interfaces are especially useful for individuals with motor impairments, allowing them to interact with computers using only their eye movements.

4. **Human-Computer Interaction**: FaceMesh can enhance human-computer interaction by enabling gestures and facial expressions as input methods, providing a more intuitive and natural interaction experience.

5. **Healthcare**: In medical fields, FaceMesh could aid in diagnosing conditions like strabismus (crossed eyes) by analyzing eye movements and alignment.

6. **User Experience Testing**: Companies can use FaceMesh to conduct user experience testing for products, websites, and applications by analyzing users' facial expressions and reactions.

## Disclaimer

The script provided in this README demonstrates a basic implementation of an eye-controlled mouse using FaceMesh. It's important to note that the script's performance might vary based on factors such as lighting conditions, webcam quality, and individual facial features. Additionally, disabling the PyAutoGUI fail-safe feature as shown in the script is not recommended, as it's a safety feature designed to prevent unintended mouse cursor movements.