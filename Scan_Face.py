# Step 3: Face Recognition using the trained model
import cv2
import numpy as np
import os
import time
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
#import Step_1
#import Step_2

def Database(Passport_No):
    # Create main window
    root = tk.Toplevel()
    root.title("Database Search")
    root.state('zoomed')  # Maximize the window on startup

    # Create a label for the touch-to-start screen
    label = tk.Label(root, text="Database Search", font=("Helvetica", 26))
    label.pack(pady=10, anchor='n')

    # Load and create the back button
    back_image = Image.open(r"C:\Users\user\Documents\Project\Images\back.jpg")
    back_image = back_image.resize((70, 70))  # Increase button size
    back_icon = ImageTk.PhotoImage(back_image)
    back_button = tk.Button(root, image=back_icon)
    back_button.place(relx=0.0, rely=1.0, anchor="sw")# Bottom left

    # Load and create the settings button
    settings_image = Image.open(r"C:\Users\user\Documents\Project\Images\settings.jpg")
    settings_image = settings_image.resize((70, 70))  # Increase button size
    settings_icon = ImageTk.PhotoImage(settings_image)
    settings_button = tk.Button(root, image=settings_icon)
    settings_button.place(relx=1.0, rely=1.0, anchor="se")  # Bottom right

    
    # Get the data from the database
    with sqlite3.connect(r'C:\Users\user\Documents\Project\Database.db') as db:
        cursor = db.cursor()
        cursor.execute("""
            SELECT * 
            FROM Passengers
            JOIN Booking ON Passengers.Passport_No = Booking.Passport_No
            JOIN Flight ON Flight.Flight_No = Booking.Flight_No
            WHERE Passengers.Passport_No = ?
        """, [Passport_No])  # Replace with the actual passport number
        results = cursor.fetchall()
        print (results)
        db.commit()

    x = results[0] 

    # Check if any results were returned
    if str(Passport_No) == x[2]:  # Get the first result
        print("found")
    else:
        print("No passenger found.")
        exit()


    box = Label(root, text=(x[0]), font=("Helvetica", 26))  
    box.pack()

    Fname = tk.Label(root, text=f"First Name = {x[0]} ", font=("Helvetica", 20))
    Fname.place(relx=0.0, rely=0.1, anchor="w")

    Sname = tk.Label(root, text=f"Second Name = {x[1]} ", font=("Helvetica", 20))
    Sname.place(relx=0.0, rely=0.2, anchor="w")

    Pno = tk.Label(root, text=f"Passport Number = {x[2]} ", font=("Helvetica", 20))
    Pno.place(relx=0.0, rely=0.3, anchor="w")

    Date = tk.Label(root, text=f"Date = {x[8]}", font=("Helvetica", 20))
    Date.place(relx=0.0, rely=0.4, anchor="w")

    Time = tk.Label(root, text =f"Time ={x[9]}", font =("Helvetica", 20))
    Time.place(relx=0.0, rely=0.5, anchor = "w")

    Flight_No = tk.Label(root, text=f"Flight = {x[4]} ", font=("Helvetica", 20))
    Flight_No.place(relx=0.0, rely=0.6, anchor="w")

    Seat = tk.Label(root, text=f"Seat Number = {x[6]} ", font=("Helvetica", 20))
    Seat.place(relx=0.0, rely=0.7, anchor="w")

    Gate = tk.Label(root, text=f"Gate Number = {x[10]} ", font=("Helvetica", 20))
    Gate.place(relx=0.0, rely=0.8, anchor="w")

    Destination = tk.Label(root, text=f"Destination = {x[11]} ", font=("Helvetica", 20))
    Destination.place(relx=0.0, rely=0.9, anchor="w")

    root.mainloop()

# Load the trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("training_data.yml")  # Load training data

# Load the Haarcascade file for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Manually update label dictionary based on previous training
label_dict = {0: "123456789", 1: "893726451", 2:"987321654"}  # Replace with actual names from Step 2

cap = cv2.VideoCapture(0)

# Create Main Mindow
root = tk.Tk()
root.title("Scan Face")
root.state('zoomed')  # Maximize the window on startup

# Create Label for Window for the touch-to-start screen
label = tk.Label(root, text="Scan Face", font=("Helvetica", 26))
label.pack(pady=10, anchor='n')

# Instruction image (top left)
Instruction_Img = Image.open(r"C:\Users\user\Documents\Project\Images\Face_Instruction.jpg").resize((200, 210))
Instruction_photo = ImageTk.PhotoImage(Instruction_Img)
Instruction_label = tk.Label(root, image=(Instruction_photo))
Instruction_label.place(relx=0.0, rely=0.09, anchor="nw")

# Back button (bottom left)
Back_img = Image.open(r"C:\Users\user\Documents\Project\Images\back.jpg").resize((70, 70))
Back_icon = ImageTk.PhotoImage(Back_img)
Back_button = tk.Button(root, image=Back_icon)
Back_button.place(relx=0.0, rely=1.0, anchor="sw")

# Settings button (bottom right)
Settings_img = Image.open(r"C:\Users\user\Documents\Project\Images\settings.jpg").resize((70, 70))
Settings_icon = ImageTk.PhotoImage(Settings_img)
Settings_button = tk.Button(root, image=Settings_icon)
Settings_button.place(relx=1.0, rely=1.0, anchor="se")

#Label to Display the Video
video_label = tk.Label(root)
video_label.pack()

#Function for updating video feed
def show_frame():
    ret, frame = cap.read()
    if not ret:
        return

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)# Detect faces

    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]# Extract the face region
        label, confidence = recognizer.predict(face_img)

        if confidence < 70:  # Confidence threshold (lower is better)
            Passport_No = label_dict.get(label, "Unknown")
            Database(Passport_No)

        else:
            name = "Unknown"

        # Draw green rectangle and display  user name
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)#Green Rectngle
        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)# Display name

    # Convert Frame to Tkinter-compatible image
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb_frame)
    imgtk = ImageTk.PhotoImage(image=img)

    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)
    video_label.after(10, show_frame)

# --- Release camera on window close ---
def on_closing():
    cap.release()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# --- Start the loop ---
show_frame()
root.mainloop()