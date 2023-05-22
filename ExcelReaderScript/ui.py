import tkinter as tk

window = tk.Tk()
# Create title of the window
window.title('Test Result Calculator')
# Set size of the window
window.minsize(width=500, height=500)

# Label for testbenches to be included
tb_Label = tk.Label(text='Testbenches to include',
                    font=('Arial', 8, 'bold'))
tb_Label.grid(column=0, row=0)


# Checkbuttons for testbenches
def checkbutton_1_used():
    print(checked_state_1.get())


def checkbutton_2_used():
    print(checked_state_2.get())


# Checkbutton SYS-110
checked_state_1 = tk.IntVar()
checkbutton_1 = tk.Checkbutton(text='SYS-110',
                               variable=checked_state_1,
                               command=checkbutton_1_used)
checkbutton_1.grid(column=0, row=1)

# Checkbutton SYS-112
checked_state_2 = tk.IntVar()
checkbutton_2 = tk.Checkbutton(text='SYS-112',
                               variable=checked_state_2,
                               command=checkbutton_2_used)
checkbutton_2.grid(column=0, row=2)


# Loop for waiting for interaction of the user
window.mainloop()
