import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Message", "lol!")

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create a button
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=20)

# Run the application
root.mainloop()