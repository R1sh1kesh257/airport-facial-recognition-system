import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import tkinter.messagebox as messagebox

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
        passport_number = "123456789"  # Replace with dynamic value in actual use

        with sqlite3.connect(r'C:\Users\user\Documents\Project\Database.db') as connect:
            cursor = connect.cursor()
            cursor.execute("""
                UPDATE Booking 
                SET Seat_No = ? 
                WHERE Passport_No = ?
            """, (seat, passport_number))
            connect.commit()

        messagebox.showinfo("Success", f"Seat {seat} successfully assigned.")
        print(f"Seat {seat} updated in the database for passport {passport_number}")

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
root = tk.Tk()
root.title("Flight Seat Selector")
root.state('zoomed')  # Maximize the window

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
Back_button = tk.Button(root, image=Back_icon)
Back_button.place(relx=0.0, rely=1.0, anchor="sw")

# Settings button (bottom right)
Settings_img = Image.open(r"C:\Users\user\Documents\Project\Images\settings.jpg").resize((70, 70))
Settings_icon = ImageTk.PhotoImage(Settings_img)
Settings_button = tk.Button(root, image=Settings_icon)
Settings_button.place(relx=1.0, rely=1.0, anchor="se")

# Run the app
root.mainloop()
