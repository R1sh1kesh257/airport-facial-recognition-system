# Step 1: Capture Images for Face Recognition
import cv2
import os

# Create a Dataset Folder and PATH for it
dataset_path = r"C:\Users\user\Documents\Project\Dataset"
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# Initialize webcam
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

person_name = input("Enter person's Passport Number: ")  # Name of the person
save_path = os.path.join(dataset_path, person_name)
if not os.path.exists(save_path):
    os.makedirs(save_path)

count = 0  # Image count

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to Grayscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        face_img = gray[y:y+h, x:x+w]  # Crop the face
        cv2.imwrite(f"{save_path}/img_{count}.jpg", face_img)  # Save face

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Capturing Faces", frame)

    if count >= 200:  # Capture 200 images per person
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()