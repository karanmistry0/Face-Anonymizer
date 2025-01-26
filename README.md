# Face Detection and Anonymization

## Overview
This script detects faces in images, videos, or live webcam feeds and applies a blur effect to anonymize them. It uses MediaPipe's face detection solution and OpenCV for video processing and visualization.

## Features
- Detects faces in images, video files, or webcam streams.
- Anonymizes faces by applying a blur effect.
- Saves the processed output for both images and videos.

## Libraries Used
- `cv2` (OpenCV): For image and video processing.
- `mediapipe`: For face detection.
- `argparse`: For command-line argument parsing.
- `os`: For file operations.

## How to Run
1. **Install Dependencies**:
   Ensure you have Python installed. Use the following command to install the required libraries:
   ```bash
   pip install opencv-python mediapipe
   ```

2. **Run the Script**:
   The script accepts the following modes:
   - **Image Mode**: Processes a single image.
   - **Video Mode**: Processes a video file.
   - **Webcam Mode**: Processes a live webcam feed.

   **Examples**:
   - **Image Mode**:
     ```bash
     python main.py --mode image --filepath /path/to/image.jpg
     ```
   - **Video Mode**:
     ```bash
     python main.py --mode video --filepath /path/to/video.mp4
     ```
   - **Webcam Mode**:
     ```bash
     python main.py --mode webcam
     ```

3. **View or Save Output**:
   - In **image mode**, the processed image is saved as `anonymized_face.jpg` in the `data` folder.
   - In **video mode**, the processed video is saved as `output.mp4` in the `data` folder.
   - In **webcam mode**, the live feed displays the detected and anonymized faces. Press `q` to quit.

## Customization
- **Adjust Detection Confidence**:
  Modify the `min_detection_confidence` parameter to change the confidence threshold for face detection. Example:
  ```python
  with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.8) as face_detection:
  ```
- **Change Blur Intensity**:
  Update the kernel size in the `cv2.blur` function to control the intensity of the blur effect.
  ```python
  cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (30, 30))
  ```

## Notes
- Ensure the `data` folder exists in the same directory as the script to save output files.
- For optimal performance, ensure the input video or image resolution is not excessively high.

## Acknowledgments
This project leverages MediaPipe for efficient face detection and OpenCV for processing, making it a robust tool for face anonymization.

