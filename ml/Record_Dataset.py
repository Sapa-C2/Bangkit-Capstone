import os
import cv2
import numpy as np
import time

# Set the current working directory to the directory containing the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize MediaPipe Hands
import mediapipe as mp
mphands = mp.solutions.hands
hands = mphands.Hands()
mp_drawing = mp.solutions.drawing_utils

# OpenCV video capture
cap = cv2.VideoCapture(0)
# Define the output directory for storing the dataset
output_parent_dir = "dataset_coba"
if not os.path.exists(output_parent_dir):
    os.makedirs(output_parent_dir)

# Define the gesture labels
gesture_labels = ['A', 'B', 'C', 'D', 'E']

# Create a directory for each letter
for label in gesture_labels:
    output_dir = os.path.join(output_parent_dir, label)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

# Define the number of frames to capture for each gesture
frames_per_gesture = 10000

# Function to save frames with labels
def save_frames(frames, label):
    global img_counter
    for frame_index, frame in enumerate(frames):
        img_name = os.path.join(output_parent_dir, label, f"{label}_{frame_index}.jpg")
        cv2.imwrite(img_name, frame)
        print(f"Saved frame {frame_index} for gesture {label}")

# Main loop for data recording
for gesture_label in gesture_labels:
    frames = []
    frame_count = 0
    print(f"Recording {gesture_label}...")
    
    while frame_count < frames_per_gesture:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hand landmarks using MediaPipe
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks (finger joints)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mphands.HAND_CONNECTIONS)

                # Append frame to list
                frames.append(frame.copy())
                frame_count += 1

        # Display the frame
        cv2.imshow('Hand Gesture Recording', frame)

        # Check for key presses
        key = cv2.waitKey(1)
        if key == ord('q'):  # Quit
            break

    # Save frames for the gesture
    print(f"Saving {frame_count} frames for gesture {gesture_label}...")
    save_frames(frames, gesture_label)

    # Release resources after recording
    cv2.destroyAllWindows()

# Release resources after recording all gestures
cap.release()
