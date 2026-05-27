from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import time
import os
import sqlite3

#Function for settings page when settings button is clicked
def settings_page():
    for window in root.winfo_children():
        window.destroy()

    # Title of window
    Label4 = tk.Label(root, text="Settings", font=("Helvetica", 26))
    Label4.pack(pady=20)

    def change_color():
        global newbg
        newbg="lightblue"
        root.config(bg=newbg)  # Change background color
        button_frame.config(bg=newbg)  # Change button frame color
        top_row.config(bg=newbg)  # Change top row color
        bottom_row.config(bg=newbg) # Change bottom row color
    

    # Create a frame to hold all setting buttons in the center
    button_frame = tk.Frame(root)
    button_frame.pack(expand=True)

    # Create two subframes for top and bottom rows
    top_row = tk.Frame(button_frame)
    bottom_row = tk.Frame(button_frame)
    top_row.pack(pady=20)
    bottom_row.pack(pady=20)

    # Colour Change Button 
    Colour_change_img = Image.open(r"C:\Users\user\Documents\Project\Images\Colour_Change.jpg").resize((250, 250))
    Colour_change_icon = ImageTk.PhotoImage(Colour_change_img)
    Colour_change_btn = tk.Button(top_row, image=Colour_change_icon, command=lambda: change_color())
    Colour_change_btn.pack(side="left", padx=40)

    # Font Change Button 
    Font_change_img = Image.open(r"C:\Users\user\Documents\Project\Images\Font_Change.jpg").resize((250, 250))
    Font_change_icon = ImageTk.PhotoImage(Font_change_img)
    Font_change_btn = tk.Button(top_row, image=Font_change_icon, command=lambda: print("Font Change Clicked!"))
    Font_change_btn.pack(side="left", padx=40)

    # Font Size Button
    Font_size_img = Image.open(r"C:\Users\user\Documents\Project\Images\Font_Size_Change.jpg").resize((250, 250))
    Font_size_icon = ImageTk.PhotoImage(Font_size_img)
    Font_size_btn = tk.Button(bottom_row, image=Font_size_icon, command=lambda: print("Font Size Clicked!"))
    Font_size_btn.pack(side="left", padx=40)

    # Language Change Button
    Language_change_img = Image.open(r"C:\Users\user\Documents\Project\Images\Language_change.jpg").resize((250, 250))
    Language_change_icon = ImageTk.PhotoImage(Language_change_img)
    Language_change_btn = tk.Button(bottom_row, image=Language_change_icon, command=lambda: print("Language Change Clicked!"))
    Language_change_btn.pack(side="left", padx=40)

    # Back Button (Bottom-Left)
    back_image = Image.open(r"C:\Users\user\Documents\Project\Images\back.jpg").resize((70, 70))
    back_icon = ImageTk.PhotoImage(back_image)
    back_button = tk.Button(root, image=back_icon)
    back_button.place(relx=0.0, rely=1.0, anchor="sw")

    # Settings Button (Bottom-Right)
    settings_image = Image.open(r"C:\Users\user\Documents\Project\Images\settings.jpg").resize((70, 70))
    settings_icon = ImageTk.PhotoImage(settings_image)
    settings_button = tk.Button(root, image=settings_icon, command= settings_page)
    settings_button.place(relx=1.0, rely=1.0, anchor="se")

    root.mainloop()

# Create main window
root = tk.Tk()
root.title("Airport Facial Recognition System")
root.state('zoomed')  # Maximize the window on startup
currentbg = root.cget("bg")  # the current default background color
root.configure(bg=currentbg)


# Function to handle the start screen and button placement
def start_app(event):

    """Removes the start screen and shows the main screen with buttons."""
    start_label.pack_forget()  # Remove the starting label

    # Place the settings button in the bottom-right corner
    settings_button.place(relx=1.0, rely=1.0, anchor="se")

    # Place the back button in the bottom-left corner
    back_button.place(relx=0.0, rely=1.0, anchor="sw") 

    root.unbind("<Button-1>")  # Prevent further triggers
    
    scan_face()  # Start scanning when clicked


# Function to ensure buttons are placed after the window is fully initialized
def place_initial_buttons():
    """Ensures buttons are placed after the window is fully initialized."""
    settings_button.place(relx=1.0, rely=1.0, anchor="se")  # Bottom-right

# Create a label for the touch-to-start screen
start_label = tk.Label(root, text="Touch to Start", font=("Helvetica", 26))
start_label.pack(expand=True)

# Load settings icon for the starting page
settings_image = Image.open(r"C:\Users\user\Documents\Project\Images\settings.jpg")
settings_image = settings_image.resize((70, 70))  # Increase image size to 70x70
settings_icon = ImageTk.PhotoImage(settings_image)
settings_button = tk.Button(image=settings_icon, command=settings_page)

# Load back icon for the starting page
back_image = Image.open(r"C:\Users\user\Documents\Project\Images\back.jpg")
back_image = back_image.resize((70, 70))  # Increase image size to 70x70
back_icon = ImageTk.PhotoImage(back_image)
back_button = tk.Button(root, image=back_icon)

# Ensure buttons are placed correctly after window in itializes
root.after(100, place_initial_buttons)

# Bind mouse click event to start the app
root.bind("<Button-1>", start_app)  # Start scanning when clicked


# Function for scanning the users face
def scan_face():
    for window in root.winfo_children():
        window.destroy()

    # Load the trained model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("training_data.yml")  # Load training data

    # Load the Haarcascade file for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Manually update label dictionary based on previous training
    label_dict = {0: "123456789", 1: "893726451", 2:"987321654", 3:"123789456"}  # Passport numbers that represent the users

    cap = cv2.VideoCapture(0)

    # Create Main Mindow
    root.title("Scan Face")
    root.state('zoomed')  # Maximize the window on startup
    root.configure(bg=newbg)  # Set the background color    

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
    Settings_button = tk.Button(image=settings_icon, command=settings_page)
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
                global Passport_No
                Passport_No = label_dict.get(label, "Unknown")
                flight_seat_selector(Passport_No)  # Call the flight seat selector function
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

    # Function to release the camera and close the window
    def on_closing():
        cap.release()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Start the loop 
    show_frame()
    root.mainloop()


# Function to handle flight seat selection
def flight_seat_selector(Passport_No):
    for window in root.winfo_children():
        window.destroy()

    # Global variables
    selected_seats = set()
    seat_buttons = {}
    booked_seats = set()

    # Function to view which seats are booked
    def get_booked_seats():
        try:
            with sqlite3.connect(r'C:\Users\user\Documents\Project\Database.db') as connect:
                cursor = connect.cursor()
                cursor.execute("SELECT Seat_No FROM Booking WHERE Seat_No IS NOT NULL")
                results = cursor.fetchall()
                return {row[0] for row in results}
        except sqlite3.OperationalError as e:
            messagebox.showerror("Database Error", f"Could not fetch booked seats.\nError: {e}")
            return set()

    # Function to update the seat in the database
    def update_seat(seat):
        try:

            with sqlite3.connect(r'C:\Users\user\Documents\Project\Database.db') as connect:
                cursor = connect.cursor()
                cursor.execute("""
                    UPDATE Booking 
                    SET Seat_No = ? 
                    WHERE Passport_No = ?
                """, (seat, Passport_No))
                connect.commit()

            messagebox.showinfo("Success", f"Seat {seat} successfully assigned.")
            Database(Passport_No)  # Call the database function to display information

        except sqlite3.OperationalError as e:
            messagebox.showerror("Database Error", f"Could not update seat.\nError: {e}")
            print("Database Error:", e)

    # Handle Next button
    def on_next():
        if selected_seats:
            selected_seat = list(selected_seats)[0]
            update_seat(selected_seat)
        else:
            messagebox.showwarning("No Seat Selected", "Please select a seat before proceeding.")

    # Toggle seat selection
    def toggle_seat(seat):
        if seat in selected_seats:
            selected_seats.remove(seat)
            seat_buttons[seat].config(bg="SystemButtonFace")
        else:
            selected_seats.clear()
            for s in seat_buttons:
                if s not in booked_seats:
                    seat_buttons[s].config(bg="SystemButtonFace")
            selected_seats.add(seat)
            seat_buttons[seat].config(bg="green")
        print("Selected Seats:", selected_seats)

    # Create the main window
    root.title("Flight Seat Selector")
    root.state('zoomed')  # Maximize the window
    root.configure(bg=newbg)  # Set the background color 

    # Grid layout to center everything
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=0)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=0)
    root.grid_columnconfigure(2, weight=1)

    # Outer container
    container = tk.Frame(root)
    container.grid(row=1, column=1)

    # Title label
    start_label = tk.Label(container, text="Choose your Flight Seat", font=("Helvetica", 28, "bold"))
    start_label.grid(row=0, column=0, pady=(0, 30))

    # Seat grid frame
    seat_frame = tk.Frame(container)
    seat_frame.grid(row=1, column=0)

    # Get booked seats
    booked_seats = get_booked_seats()

    # Seat grid layout
    rows = 5  # Rows A to E
    cols = 4  # Columns 1 to 4

    for r in range(rows):
        for c in range(cols):
            seat_label = f"{chr(65 + r)}{c + 1}"
            btn = tk.Button(seat_frame, text=seat_label, width=8, height=3, font=("Arial", 12), bd=3)

            if seat_label in booked_seats:
                btn.config(bg="red", state="disabled")
            else:
                btn.config(command=lambda s=seat_label: toggle_seat(s))

            btn.grid(row=r, column=c, padx=10, pady=10)
            seat_buttons[seat_label] = btn

    # Next button
    next_button = tk.Button(container, text="Next", font=("Helvetica", 16), command=on_next)
    next_button.grid(row=2, column=0, pady=(20, 0))

    # Back button (bottom left)
    Back_img = Image.open(r"C:\Users\user\Documents\Project\Images\back.jpg").resize((70, 70))
    Back_icon = ImageTk.PhotoImage(Back_img)
    Back_button = tk.Button(root, image=Back_icon, command=lambda: scan_face())
    Back_button.place(relx=0.0, rely=1.0, anchor="sw")

    # Settings button (bottom right)
    Settings_img = Image.open(r"C:\Users\user\Documents\Project\Images\settings.jpg").resize((70, 70))
    Settings_icon = ImageTk.PhotoImage(Settings_img)
    Settings_button = tk.Button(root, image=Settings_icon)
    Settings_button.place(relx=1.0, rely=1.0, anchor="se")

    # Run the app
    root.mainloop()


# Function to display the database information
def Database(Passport_No):
    for window in root.winfo_children():
        window.destroy()
    
    # Create a label for the database search screen
    label = tk.Label(root, text="Database Search", font=("Helvetica", 26))
    label.pack(pady=10, anchor='n')

    root.configure(bg=newbg)  # Set the background color 

    # Load and create the back button
    back_image = Image.open(r"C:\Users\user\Documents\Project\Images\back.jpg")
    back_image = back_image.resize((70, 70))  # Increase button size
    back_icon = ImageTk.PhotoImage(back_image)
    back_button = tk.Button(root, image=back_icon, command=lambda: flight_seat_selector(Passport_No))  
    back_button.image = back_icon  # Keep reference
    back_button.place(relx=0.0, rely=1.0, anchor="sw")  # Bottom left

    # Load and create the settings button
    settings_image = Image.open(r"C:\Users\user\Documents\Project\Images\settings.jpg")
    settings_image = settings_image.resize((70, 70))  # Increase button size
    settings_icon = ImageTk.PhotoImage(settings_image)
    settings_button = tk.Button(root, image=settings_icon, command=settings_page)
    settings_button.image = settings_icon  # Keep reference
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
        """, [Passport_No])  #This is the query to get the data from the database using the users passport number
        results = cursor.fetchall()
        db.commit()

    x = results[0] 

    # Create labels for the passenger details
    Fname = tk.Label(root, text=f"First Name = {x[0]}", font=("Helvetica", 20))
    Fname.pack(anchor="w", padx=20, pady=5)

    Sname = tk.Label(root, text=f"Second Name = {x[1]}", font=("Helvetica", 20))
    Sname.pack(anchor="w", padx=20, pady=5)

    Pno = tk.Label(root, text=f"Passport Number = {x[2]}", font=("Helvetica", 20))
    Pno.pack(anchor="w", padx=20, pady=5)

    Date = tk.Label(root, text=f"Date = {x[8]}", font=("Helvetica", 20))
    Date.pack(anchor="w", padx=20, pady=5)

    Time = tk.Label(root, text=f"Time = {x[9]}", font=("Helvetica", 20))
    Time.pack(anchor="w", padx=20, pady=5)

    Flight_No = tk.Label(root, text=f"Flight = {x[4]}", font=("Helvetica", 20))
    Flight_No.pack(anchor="w", padx=20, pady=5)

    Seat = tk.Label(root, text=f"Seat Number = {x[6]}", font=("Helvetica", 20))
    Seat.pack(anchor="w", padx=20, pady=5)

    Gate = tk.Label(root, text=f"Gate Number = {x[10]}", font=("Helvetica", 20))
    Gate.pack(anchor="w", padx=20, pady=5)

    Destination = tk.Label(root, text=f"Destination = {x[11]}", font=("Helvetica", 20))
    Destination.pack(anchor="w", padx=20, pady=5)

    next_button = tk.Button(root, text="Next", font=("Helvetica", 16), command=lambda: thank_you())
    next_button.pack(pady=20)

    root.mainloop()


# Function to display the thank you page
def thank_you():
    for window in root.winfo_children():
        window.destroy()

    def place_buttons():
        """Place the buttons after the window is fully initialized."""
        settings_button.place(x=border_frame.winfo_width() - 86, y=border_frame.winfo_height() - 36)  # Bottom-right
        back_button.place(x=20, y=border_frame.winfo_height() - 95)  # Bottom-left

    root.configure(bg=newbg)  # Set the background color 

    # Name of Window
    Label4 = tk.Label(root, text="Thank You", font=("Helvetica", 16))
    Label4.pack(pady=10, anchor="n")

    # Create an outer frame for the border
    border_frame = tk.Frame(root, bg="green")  
    border_frame.pack(fill="both", expand=True, padx=10, pady=10) 

    # Create an inner frame for content
    content_frame = tk.Frame(border_frame, bg="white")  # White inner area
    content_frame.pack(fill="both", expand=True, padx=20, pady=20)  # Padding inside the border

    # Label for thank you message
    label = tk.Label(content_frame, text="Thank You for using This Interface\n Have a Safe Journey", font=("Helvetica", 20), bg="white")
    label.pack(expand=True, anchor="center")

    # Load settings icon
    settings_image = Image.open(r"C:\Users\user\Documents\Project\Images\settings.jpg")
    settings_image = settings_image.resize((70, 70))  
    settings_icon = ImageTk.PhotoImage(settings_image)
    settings_button = tk.Button(image=settings_icon, command=settings_page)

    # Load back icon
    back_image = Image.open(r"C:\Users\user\Documents\Project\Images\back.jpg")
    back_image = back_image.resize((70, 70))  
    back_icon = ImageTk.PhotoImage(back_image)
    back_button = tk.Button(border_frame, image=back_icon, command=lambda: Database(Passport_No))  

    # Delay the button placement to ensure the window size is available
    root.after(100, place_buttons)  # Wait for 100ms to place buttons after window size is available

    # Run the application
    root.mainloop()

root.mainloop()