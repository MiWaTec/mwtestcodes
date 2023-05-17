from tkinter import *

window = Tk()
# Create title of the window
window.title("My first GUI program")
# Set the size of the window
window.minsize(width=500, height=500)

# Label
my_label = Label(text="I am a label.", font=("Arial", 24, "bold"))
my_label.pack()
# Change/update properties of a particular component that was created
my_label["text"] = "New Text"


# Button
def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=30)
input.insert(END, string="Some text to begin with.")
print(input.get())
input.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox
text.focus()
# Adds some text to begin with
text.insert(END, "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_used():
    # Gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value
# (passes the value to the function, when scale is used)
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
print(scale)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state,
                          command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())

# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state,
                           command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state,
                           command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# Window waits for interaction of the user. The mainloop should be
# at the end of the code.
window.mainloop()
