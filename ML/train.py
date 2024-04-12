import os
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from PIL import Image
import numpy as np


# Step 1: Data Preparation
captcha_dir = "captcha/"
captcha_images = []
labels = []

for filename in os.listdir(captcha_dir):
    if filename.endswith(".png"):  # Assuming images are in PNG format
        captcha_labels = filename.split(".")[0]
        labels.append(captcha_labels)
        img = Image.open(os.path.join(captcha_dir, filename))
        captcha_images.append(np.array(img))

# Step 2: Data Preprocessing
captcha_images = np.array(captcha_images) / 255.0  # Normalization
labels = LabelBinarizer().fit_transform(labels)  # One-hot encoding
num_classes = labels.shape[1]  # Calculate num_classes

# Step 3: Model Building
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(75, 250, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

# Step 4: Model Training
X_train, X_test, y_train, y_test = train_test_split(captcha_images, labels, test_size=0.2, random_state=42)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Step 5: Model Evaluation
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc}") # 0 - 1

# Step 6: Model Deployment (Optional)
# Save the model for future use
model.save("captcha_model.h5")
