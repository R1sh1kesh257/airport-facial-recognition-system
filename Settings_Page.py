from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Settings")
root.state('zoomed')

def change_color():
    newbg="lightblue"
    root.config(bg=newbg)  # Change background color
    button_frame.config(bg=newbg)  # Change button frame color
    top_row.config(bg=newbg)  # Change top row color
    bottom_row.config(bg=newbg) # Change bottom row color

# Title label
Label4 = tk.Label(root, text="Settings", font=("Helvetica", 26))
Label4.pack(pady=20)

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
back_button = tk.Button(root, image=back_icon, command=lambda: print("Back Clicked"))
back_button.place(relx=0.0, rely=1.0, anchor="sw")

# Settings Button (Bottom-Right)
settings_image = Image.open(r"C:\Users\user\Documents\Project\Images\settings.jpg").resize((70, 70))
settings_icon = ImageTk.PhotoImage(settings_image)
settings_button = tk.Button(root, image=settings_icon, command=lambda: print("Settings Clicked!"))
settings_button.place(relx=1.0, rely=1.0, anchor="se")

root.mainloop()