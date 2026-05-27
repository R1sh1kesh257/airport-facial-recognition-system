import tkinter as tk
from PIL import Image, ImageTk
import sqlite3

root = tk.Tk()
root.state("zoomed")
root.title("Database Search")

# Create a label for the database search screen
label = tk.Label(root, text="Database Search", font=("Helvetica", 26))
label.pack(pady=10, anchor='n')

# Load and create the back button
back_image = Image.open(r"C:\Users\user\Documents\Project\Images\back.jpg")
back_image = back_image.resize((70, 70))  # Increase button size
back_icon = ImageTk.PhotoImage(back_image)
back_button = tk.Button(root, image=back_icon)  # <- FIXED
back_button.image = back_icon  # Keep reference
back_button.place(relx=0.0, rely=1.0, anchor="sw")  # Bottom left

# Load and create the settings button
settings_image = Image.open(r"C:\Users\user\Documents\Project\Images\settings.jpg")
settings_image = settings_image.resize((70, 70))  # Increase button size
settings_icon = ImageTk.PhotoImage(settings_image)
settings_button = tk.Button(root, image=settings_icon, command=lambda: print("Settings clicked")) 
settings_button.image = settings_icon  # Keep reference
settings_button.place(relx=1.0, rely=1.0, anchor="se")  # Bottom right

Passport_No = 893726451  # replace with the actual passport number you want to search for

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

next_button = tk.Button(root, text="Next", font=("Helvetica", 16), command=lambda: print("Next clicked"))
next_button.pack(pady=20)

root.mainloop()
