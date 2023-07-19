

# MotionDETECTION - Real-Time Pedestrian Detection with Motion Direction Visualization

![mD](https://github.com/AbrarAmiya/MotionDETECTION/assets/115402065/9f0b8b6c-069d-41f8-bf5c-a5ab5e072f2e)
![MotionDETECTION](https://github.com/AbrarAmiya/MotionDETECTION/blob/main/assets/demo.gif)

MotionDETECTION is a Python program that uses computer vision techniques to perform real-time pedestrian detection in a video stream or webcam input. It utilizes the HOG (Histogram of Oriented Gradients) algorithm to detect people in the frame, and it also provides a visual representation of their motion direction.

## Features
- Real-time pedestrian detection using a pre-trained HOG-based detector.
- Visualization of detected pedestrians with bounding boxes.
- Motion direction indication for each detected pedestrian.
- Smooth motion tracking across frames.

## Requirements
To run MotionDETECTION, you'll need the following libraries installed:
- OpenCV (cv2)

You can install the required libraries using pip:
```bash
pip install opencv-python
```

## Usage
1. Clone this repository to your local machine.
2. Make sure you have Python installed, along with the necessary libraries.
3. Replace `"C:\\Users\\ASUS\\Downloads\\test5.mp4"` in the `video = cv2.VideoCapture(...)` line with the path to your video file or use `0` to capture input from your webcam.
4. Run the script:
```bash
python motion_detection.py
```
5. The application will open a window showing the real-time video stream with pedestrian detection and motion direction visualization.
6. Press the 'q' key to exit the application.

## How it Works
The MotionDETECTION program works as follows:
1. Loads a pre-trained HOG-based pedestrian detector provided by OpenCV.
2. Reads the video stream frame by frame.
3. Detects pedestrians in each frame using the HOG detector and draws bounding boxes around them.
4. Calculates the motion direction for each detected pedestrian based on their centroid displacement between consecutive frames.
5. Visualizes the motion direction by drawing a line from the previous centroid position to the current one.
6. Displays the processed video with real-time pedestrian detection and motion direction indication.

## Customization
You can customize the behavior of the program to suit your needs. Some possible improvements include:
- Adjusting the size of the bounding boxes and motion direction line thickness.
- Changing the motion direction thresholds to make the direction indication more or less sensitive.
- Adding more features, such as counting the number of pedestrians in the frame or saving the processed video to a file.

## Contributions
Contributions to this project are welcome! If you have any ideas for improvements or bug fixes, feel free to create an issue or a pull request.

## License
This project is licensed under the [MIT License](https://github.com/AbrarAmiya/MotionDETECTION/blob/main/LICENSE).

---

Enjoy exploring MotionDETECTION! Feel free to use it for your own projects, and don't forget to give this repository a ⭐ if you find it useful! If you encounter any issues or have suggestions, please let us know in the Issues section.

Happy coding! 🚀
