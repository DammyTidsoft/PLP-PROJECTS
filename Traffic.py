import cv2

# Initialize the video source (0 for the default camera, or a file path for a video file)
video_source = 0

# Create a video capture object
cap = cv2.VideoCapture(video_source)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Read the first frame
ret, frame1 = cap.read()
# Convert frame to grayscale
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
# Apply GaussianBlur to reduce noise and detail in the image
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

while True:
    # Read the next frame
    ret, frame2 = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    # Compute the absolute difference between the current frame and the previous frame
    delta_frame = cv2.absdiff(gray1, gray2)
    # Apply a threshold to the delta image to get a binary image
    thresh_frame = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)[1]
    # Dilate the thresholded image to fill in holes, then find contours on thresholded image
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        # If the contour is big enough, draw a rectangle around it
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # Display the frame
    cv2.imshow("Frame", frame2)
    # Copy frame2 to frame1 for the next iteration
    gray1 = gray2.copy()

    # Wait for the 'q' key to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
