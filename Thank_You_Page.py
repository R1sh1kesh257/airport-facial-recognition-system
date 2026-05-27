from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

def place_buttons():
    """Place the buttons after the window is fully initialized."""
    settings_button.place(x=border_frame.winfo_width() - 95, y=border_frame.winfo_height() - 95)  # Bottom-right
    back_button.place(x=20, y=border_frame.winfo_height() - 95)  # Bottom-left

root = tk.Tk()
root.state('zoomed')  # Maximize the window on startup

Label4 = tk.Label(root, text="Thank You", font=("Helvetica", 16))
Label4.pack(pady=10, anchor="n")

# Create an outer frame for the border
border_frame = tk.Frame(root, bg="green")  
border_frame.pack(fill="both", expand=True, padx=10, pady=10) 

# Create an inner frame for content
content_frame = tk.Frame(border_frame, bg="white")  # White inner area
content_frame.pack(fill="both", expand=True, padx=20, pady=20)  # Padding inside the border

label = tk.Label(content_frame, text="Thank You for using This Interface\n Have a Safe Journey", font=("Helvetica", 16), bg="white")
label.pack(expand=True, anchor="center")

# Load settings icon
settings_image = Image.open(r"C:\Users\user\Documents\Project\Images\settings.jpg")
settings_image = settings_image.resize((70, 70))  
settings_icon = ImageTk.PhotoImage(settings_image)
settings_button = tk.Button(border_frame, image=settings_icon, command=lambda: print("Settings Clicked"))

# Load back icon
back_image = Image.open(r"C:\Users\user\Documents\Project\Images\back.jpg")
back_image = back_image.resize((70, 70))  
back_icon = ImageTk.PhotoImage(back_image)
back_button = tk.Button(border_frame, image=back_icon, command=lambda: print("Back Clicked"))

# Delay the button placement to ensure the window size is available
root.after(100, place_buttons)  # Wait for 100ms to place buttons after window size is available

# Run the application
root.mainloop()