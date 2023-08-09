# Eye Controlled Mouse

**Rodrigo Pires Vanzelotti**

This code is a Python program that uses the libraries OpenCV, Mediapipe, and the pyautogui module to control the computer's mouse based on the detected eye movements from a webcam.

Here's a detailed explanation of the code:

## Imports:

```python
import cv2
import mediapipe as mp
import pyautogui
```
**cv2:** OpenCV library used for image and video manipulation.

**mediapipe as mp:** Mediapipe library, which provides pre-built solutions for computer vision tasks.

**pyautogui:** A library for mouse and keyboard control through code.

## Webcam initialization and FaceMesh setup:

```python
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
```

**cv2.VideoCapture(0):** Initializes the webcam. The value 0 indicates that the first available camera will be used.

**mp.solutions.face_mesh.FaceMesh(refine_landmarks=True):** Initializes the FaceMesh face landmark detector with refine_landmarks enabled to improve the accuracy of the detected landmarks.

## Capturing and processing webcam frames in a loop:

```python
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
```

**cam.read():** Reads a frame from the webcam. The first returned value, denoted by _,, is a discard variable as it's not used in the code. The second returned value is stored in the variable frame.

**cv2.flip(frame, 1):** Flips the frame horizontally, as the face landmark tracking data is calibrated for a specific orientation.

**cv2.cvtColor(frame, cv2.COLOR_BGR2RGB):** Converts the frame from BGR (the default format in OpenCV) to RGB format, which is expected by Mediapipe.

**face_mesh.process(rgb_frame):** Processes the frame using the FaceMesh face landmark detector, returning an output object that contains information about the detected landmarks.

**output.multi_face_landmarks:** Gets the list of detected face landmarks in the frame.

## Detecting and tracking eye landmark points:

```python
if landmark_points:
    landmarks = landmark_points[0].landmark
    for id, landmark in enumerate(landmarks[474:478]):
        x = int(landmark.x * frame_w)
        y = int(landmark.y * frame_h)
        cv2.circle(frame, (x, y), 3, (0, 255, 0))
        if id == 1:
            screen_x = screen_w * landmark.x
            screen_y = screen_h * landmark.y
            pyautogui.moveTo(screen_x, screen_y)
```

- Checks if face landmarks have been detected in the frame.

- Accesses specific eye landmarks and iterates over them.

- For each eye landmark, draws a green circle on the frame for visualization.

- Uses the second eye landmark (landmark[475]) to control the mouse movement. The mouse position is updated to align with this landmark relative to the screen size.

## Detecting and tracking the left eye corner landmark points:

```python
left = [landmarks[145], landmarks[159]]
for landmark in left:
    x = int(landmark.x * frame_w)
    y = int(landmark.y * frame_h)
    cv2.circle(frame, (x, y), 3, (0, 255, 255))
```

- Creates a list called left containing the top-left (landmark[145]) and bottom-left (landmark[159]) eye corner landmarks.

- For each left eye corner landmark, draws a yellow circle on the frame for visualization.

## Checking for left eye blink and simulating a mouse click:

```python
if (left[0].y - left[1].y) < 0.004:
    pyautogui.click()
    pyautogui.sleep(1)
```

- Calculates the vertical difference between the top-left and bottom-left eye corner landmarks.

- If this difference is less than 0.004 (adjustable threshold for sensitivity), it is considered that the eye has closed (blinked).

- In this case, the program simulates a mouse click using the pyautogui.click() function. Then it waits for 1 second before continuing.

## Displaying the frame with the markings in a window:

```python
cv2.imshow('Eye Controlled Mouse', frame)
if cv2.waitKey(20) & 0xFF==ord('q'):
    break
```

Displays the frame with all the markings in the window titled "Eye Controlled Mouse".