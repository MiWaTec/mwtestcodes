import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Fruit Selector")

# Create a label
label = tk.Label(root, text="Select a fruit:")
label.pack(pady=10)

# Create a StringVar to store the selected fruit
selected_fruit = tk.StringVar()

# Create a dropdown menu
fruits = ["Apple", "Banana", "Orange"]
fruit_dropdown = ttk.Combobox(root, textvariable=selected_fruit, values=fruits)
fruit_dropdown.pack()

# Function to handle the selection
def on_fruit_select(event):
    selected = selected_fruit.get()
    if selected:
        label.config(text=f"You selected: {selected}")

# Bind the selection event to the function
fruit_dropdown.bind("<<ComboboxSelected>>", on_fruit_select)

# Start the Tkinter main loop
root.mainloop()
