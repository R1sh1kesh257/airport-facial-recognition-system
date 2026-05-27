import tkinter as tk
from PIL import Image, ImageTk

# Create main window
root = tk.Tk()
root.title("Touch to Start")
root.state('zoomed')  # Maximize the window on startup

# Function to handle the start screen and button placement
def start_app(event):
    """Removes the start screen and shows the main screen with buttons."""
    start_label.pack_forget()  # Remove the starting label

    # Place the settings button in the bottom-right corner
    settings_button.place(relx=1.0, rely=1.0, anchor="se")

    # Place the back button in the bottom-left corner
    back_button.place(relx=0.0, rely=1.0, anchor="sw") 

    root.unbind("<Button-1>")  # Prevent further triggers

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
settings_button = tk.Button(image=settings_icon, command=lambda: print("Settings clicked"))  # Placeholder command

# Load back icon for the starting page
back_image = Image.open(r"C:\Users\user\Documents\Project\Images\back.jpg")
back_image = back_image.resize((70, 70))  # Increase image size to 70x70
back_icon = ImageTk.PhotoImage(back_image)
back_button = tk.Button(root, image=back_icon)

# Ensure buttons are placed correctly after window initializes
root.after(100, place_initial_buttons)

# Bind mouse click event to start the app
root.bind("<Button-1>", start_app)  # Start scanning when clicked

root.mainloop()  # Start the Tkinter main loop