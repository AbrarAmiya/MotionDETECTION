
import cv2

# Load the pre-trained HOG-based pedestrian detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


video = cv2.VideoCapture("C:\\Users\\ASUS\\Downloads\\test5.mp4")  # Replace with your video file path or use 0 for camera input
 # Replace with your video file path or use 0 for camera input

# Variables for previous frame and centroid
prev_frame = None
prev_centroid = None

while video.isOpened():
    # Read current frame
    ret, frame = video.read()

    if not ret:
        break

    # Resize frame to a smaller size for faster processing (optional)
    frame = cv2.resize(frame, (640, 480))

    # Convert frame to grayscale for motion detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect people in the frame
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8), padding=(4, 4), scale=1.05)

    # Draw bounding boxes around detected people and compute motion direction
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Compute centroid of the bounding box
        centroid = (x + w // 2, y + h // 2)

        if prev_frame is not None and prev_centroid is not None:
            # Compute motion direction based on centroid displacement
            motion_direction = ""
            if centroid[0] > prev_centroid[0] + 10:
                motion_direction = "Right"
            elif centroid[0] < prev_centroid[0] - 10:
                motion_direction = "Left"
            elif centroid[1] > prev_centroid[1] + 10:
                motion_direction = "Down"
            elif centroid[1] < prev_centroid[1] - 10:
                motion_direction = "Up"

            # Draw line indicating the motion direction
            cv2.line(frame, prev_centroid, centroid, (255, 0, 0), 2)
            cv2.putText(frame, motion_direction, (centroid[0] + 10, centroid[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # Update previous centroid
        prev_centroid = centroid

    # Display the resulting frame
    cv2.imshow("Pedestrian Detection", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Update previous frame
    prev_frame = gray

# Release video capture and close windows
video.release()
cv2.destroyAllWindows()

