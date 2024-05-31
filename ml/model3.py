import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping

# Define the directory containing the dataset
dataset_dir = "dataset_coba"

# Load the dataset and dynamically determine the number of photos for each class
class_counts = {}
for label in os.listdir(dataset_dir):
    label_dir = os.path.join(dataset_dir, label)
    class_counts[label] = len(os.listdir(label_dir))

# Define the number of photos for each class as the minimum count among all classes
num_photos_per_class = min(class_counts.values())
num_classes = len(class_counts)

# Define a dictionary to map class labels to integers
class_to_int = {label: idx for idx, label in enumerate(sorted(class_counts.keys()))}

# Load and preprocess the dataset
images = []
labels = []


for label in os.listdir(dataset_dir):
    label_dir = os.path.join(dataset_dir, label)
    for filename in os.listdir(label_dir)[:num_photos_per_class]:
        image_path = os.path.join(label_dir, filename)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, (28, 28))
        image = image / 255.0  # Normalize pixel values to [0, 1]
        images.append(image)
        labels.append(class_to_int[label])  # Convert label to int using the dictionary

x = np.array(images).reshape(-1, 28, 28, 1)  # Reshape input data
y = np.array(labels)

# Split the dataset into training and validation sets
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)

datagen = ImageDataGenerator(
        rotation_range=10,
        zoom_range=0.1,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=False,
        vertical_flip=False
)
datagen.fit(x_train)
# Define the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Dropout(0.3),
    Flatten(),
    Dropout(0.2),
    Dense(128, activation='relu'),
    Dense(256, activation='relu'),
    Dense(num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
    x_train, y_train,
    epochs=100,
    batch_size=32,
    validation_data=(x_val, y_val),
    callbacks=[ReduceLROnPlateau(), EarlyStopping(patience=3)]
)

# Evaluate the model
loss, accuracy = model.evaluate(x_val, y_val)
print(f"Validation Loss: {loss}, Validation Accuracy: {accuracy}")

# Save the model
model.save('smnist_model.h5')
