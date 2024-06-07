import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define the directory containing the dataset
dataset_dir = "dataset_coba3"

# Define the desired number of samples per class
desired_samples_per_class = 15000

# Load and preprocess the dataset
images = []
labels = []

# Determine the number of photos per class
class_counts = {}
for label in os.listdir(dataset_dir):
    label_dir = os.path.join(dataset_dir, label)
    class_counts[label] = len(os.listdir(label_dir))
num_photos_per_class = min(class_counts.values())

# Create an ImageDataGenerator for data augmentation
datagen = ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=False,
    vertical_flip=False
)

label_encoder = LabelEncoder()
label_encoder.fit(os.listdir(dataset_dir))  # Fit the label encoder to the label names

for label in os.listdir(dataset_dir):
    label_dir = os.path.join(dataset_dir, label)
    num_generated_samples = 0
    while num_generated_samples < desired_samples_per_class:
        for filename in os.listdir(label_dir)[:num_photos_per_class]:
            image_path = os.path.join(label_dir, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (28, 28))
            image = image / 255.0  # Normalize pixel values to [0, 1]
            images.append(image)
            labels.append(label)  # Append the label name
            num_generated_samples += 1
            if num_generated_samples >= desired_samples_per_class:
                break

# Convert labels to integers using label encoder
labels_encoded = label_encoder.transform(labels)

x = np.array(images).reshape(-1, 28, 28, 1)  # Reshape input data
y = np.array(labels_encoded)

# Split the dataset into training, validation, and testing sets
x_train, x_temp, y_train, y_temp = train_test_split(x, y, test_size=0.2, random_state=42)
x_val, x_test, y_val, y_test = train_test_split(x_temp, y_temp, test_size=0.5, random_state=42)

# Apply data augmentation to the training set
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
    Dense(len(label_encoder.classes_), activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model with data augmentation
history = model.fit(
    datagen.flow(x_train, y_train, batch_size=32),
    epochs=5,
    validation_data=(x_val, y_val),
    callbacks=[ReduceLROnPlateau(), EarlyStopping(patience=3)]
)

# Evaluate the model
loss, accuracy = model.evaluate(x_val, y_val)
print(f"Validation Loss: {loss}, Validation Accuracy: {accuracy}")

# Save the model
model.save('smnist_model_augmented.h5')
