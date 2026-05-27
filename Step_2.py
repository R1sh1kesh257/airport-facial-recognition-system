# Step 2: Train the model using the images in the dataset folder
import cv2
import numpy as np
import os

dataset_path = r"C:\Users\user\Documents\Project\Dataset" # Path to the dataset folder
recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []

# Assign numeric labels to each person
label_dict = {}
label_count = 0

for person_name in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person_name)

    if not os.path.isdir(person_path):
        continue
    
    if person_name not in label_dict:
        label_dict[person_name] = label_count
        label_count += 1

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        faces.append(image)
        labels.append(label_dict[person_name])

faces = np.array(faces, dtype="object")
labels = np.array(labels)

recognizer.train(faces, labels)
recognizer.save("training_data.yml")

print("Training complete! Data saved as 'training_data.yml'")
print("Label Mapping:", "123456789")  # Prints the label assigned to each person
