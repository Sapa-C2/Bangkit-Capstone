import cv2
import numpy as np
from tensorflow.keras.models import load_model
import mediapipe as mp

# Load the trained model
model = load_model('smnist_model_augmented.h5')

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# OpenCV video capture from webcam
cap = cv2.VideoCapture(0)

# Define the alphabet labels
alphabet_labels = ['A', 'B', 'C', 'D', 'E', 'F']

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

            # Get bounding box coordinates
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

            # Draw bounding box on the hand region
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

            # Crop hand region from the frame
            hand_region = frame[y_min:y_max, x_min:x_max]

            # Preprocess the hand region for model input
            if hand_region.shape[0] > 0 and hand_region.shape[1] > 0:  # Ensure valid hand region
                resized_hand_region = cv2.resize(hand_region, (28, 28))
                gray_hand_region = cv2.cvtColor(resized_hand_region, cv2.COLOR_BGR2GRAY)
                normalized_hand_region = gray_hand_region / 255.0
                preprocessed_hand_region = normalized_hand_region.reshape(1, 28, 28, 1)

                # Make predictions using the model
                predictions = model.predict(preprocessed_hand_region)
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
