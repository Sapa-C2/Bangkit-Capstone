import os
import cv2
import numpy as np
import time
import mediapipe as mp

# Set the current working directory to the directory containing the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# OpenCV video capture
cap = cv2.VideoCapture(0)

# Define the output directory for storing the dataset
output_parent_dir = "dataset_coba4"
if not os.path.exists(output_parent_dir):
    os.makedirs(output_parent_dir)

# Define the gesture labels
gesture_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N']

# Create a directory for each letter
for label in gesture_labels:
    output_dir = os.path.join(output_parent_dir, label)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

# Define the number of videos to capture for each gesture
videos_per_gesture = 2

# Define the number of frames to capture for each gesture
frames_per_gesture = 1000

# Define the time interval between capturing each gesture (in seconds)
gesture_interval = 10  # Adjust as needed to ensure each gesture captures the same amount of photos

# Function to save frames with labels
def save_frames(frames, label, video_index, bounding_boxes):
    for frame_index, (frame, bounding_box) in enumerate(zip(frames, bounding_boxes)):
        x_min, y_min, x_max, y_max = bounding_box
        cropped_frame = frame[y_min:y_max, x_min:x_max]
        cropped_frame_rgb = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
        img_name = os.path.join(output_parent_dir, label, f"{label}_video{video_index}_{frame_index}.jpg")
        cv2.imwrite(img_name, cropped_frame_rgb)  # Save as RGB image
        print(f"Saved frame {frame_index} for gesture {label} video {video_index}")

# Main loop for data recording
for gesture_label in gesture_labels:
    for video_index in range(videos_per_gesture):
        frames = []
        bounding_boxes = []
        frame_count = 0
        start_time = time.time()
        print(f"Recording {gesture_label} video {video_index}...")

        while frame_count < frames_per_gesture:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to RGB for MediaPipe processing
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Detect hand landmarks using MediaPipe
            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw landmarks (finger joints)
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # Draw bounding box
                    x_min, y_min = frame.shape[1], frame.shape[0]
                    x_max, y_max = 0, 0
                    for landmark in hand_landmarks.landmark:
                        x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                        if x < x_min:
                            x_min = x
                        if x > x_max:
                            x_max = x
                        if y < y_min:
                            y_min = y
                        if y > y_max:
                            y_max = y
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

                    # Append frame and bounding box to lists
                    frames.append(frame.copy())
                    bounding_boxes.append((x_min, y_min, x_max, y_max))
                    frame_count += 1

            # Display the frame
            cv2.imshow('Hand Gesture Recording', frame)

            # Check for key presses
            key = cv2.waitKey(1)
            if key == ord('q'):  # Quit
                break

            # Check if the time interval has elapsed
            if time.time() - start_time >= gesture_interval:
                break

        # Save frames for the gesture
        print(f"Saving {frame_count} frames for gesture {gesture_label} video {video_index}...")
        save_frames(frames, gesture_label, video_index, bounding_boxes)

        # Pause before recording the next gesture
        remaining_time = gesture_interval - (time.time() - start_time)
        if remaining_time > 0:
            print(f"Pause before recording the next gesture: {remaining_time} seconds")
            time.sleep(remaining_time)

        # Clear lists
        frames = []
        bounding_boxes = []

    # Release resources after recording
    cv2.destroyAllWindows()

# Release resources after recording all gestures
cap.release()
