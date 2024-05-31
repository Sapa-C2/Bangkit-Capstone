import cv2
import numpy as np
from tensorflow.keras.models import load_model
import mediapipe as mp

# Load the trained model
model = load_model('smnist_model.h5')

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# OpenCV video capture from webcam
cap = cv2.VideoCapture(0)

# Define the alphabet labels
alphabet_labels = ['A', 'B', 'C', 'D', 'E']

while True:
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
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Preprocess the frame for model input
            resized_frame = cv2.resize(frame, (28, 28))
            gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
            normalized_frame = gray_frame / 255.0
            preprocessed_frame = normalized_frame.reshape(1, 28, 28, 1)

            # Make predictions using the model
            predictions = model.predict(preprocessed_frame)
            predicted_label_index = np.argmax(predictions)
            predicted_gesture_label = alphabet_labels[predicted_label_index]

            # Display the predicted gesture label on the frame
            cv2.putText(frame, predicted_gesture_label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Hand Gesture Recognition', frame)

    # Check for key presses
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
