import tkinter as tk
import tkinter.ttk as ttk
import json
from evaluate_excel import calculate_results, save_filter
import time

window = tk.Tk()
# Create title of the window
window.title('Test Result Calculator')
# Set size of the window
window.minsize(width=300, height=200)

# Label for testbenches to be included
tb_label = tk.Label(text='Testbenches to include',
                    font=('Arial', 8, 'bold'))
tb_label.grid(column=0, row=0, padx=20, pady=5)

# Label for start button
start_label = tk.Label(text='Start calculation',
                       font=('Arial', 8, 'bold'))
start_label.grid(column=1, row=0, padx=20, pady=5)


# Checkbuttons for testbenches
def checkbutton_1_used():
    state = checked_state_1.get()
    save_filter('result_filter', 'testbench', 'SYS-110.tbc', state)


def checkbutton_2_used():
    state = checked_state_2.get()
    save_filter('result_filter', 'testbench', 'SYS-112.tbc', state)


def checkbutton_3_used():
    tb_input = input_field.get()
    tb_name = tb_input + '.tbc'
    if tb_input:
        state = checked_state_3.get()
        save_filter('result_filter', 'testbench', tb_name, state)
    else:
        checkbutton_3.deselect()
        print("No input given.")


# Checkbutton SYS-110
checked_state_1 = tk.IntVar()
checkbutton_1 = tk.Checkbutton(text='SYS-110',
                               variable=checked_state_1,
                               command=checkbutton_1_used)
checkbutton_1.grid(column=0, row=1, padx=20, pady=5)

# Checkbutton SYS-112
checked_state_2 = tk.IntVar()
checkbutton_2 = tk.Checkbutton(text='SYS-112',
                               variable=checked_state_2,
                               command=checkbutton_2_used)
checkbutton_2.grid(column=0, row=2, padx=20, pady=5)

# Entry for additional testbench
checked_state_3 = tk.IntVar()
checkbutton_3 = tk.Checkbutton(text='Other:   ',
                               variable=checked_state_3,
                               command=checkbutton_3_used)
checkbutton_3.grid(column=0, row=3)
input_field = tk.Entry(width=10)
input_field.grid(column=0, row=4)


# Start button
def start_button_clicked():
    calculate_results()
    print('Calculation finished')


start_button = tk.Button(text="Calculate", command=start_button_clicked)
start_button.grid(column=1, row=1, padx=20, pady=5)

# Main program
# Check default settings
with open('filter.json', 'r') as f:
    default = json.load(f)

testbenches = default['result_filter']['testbench']
for tb in testbenches:
    if tb not in ['SYS-110.tbc', 'SYS-112.tbc']:
        save_filter('result_filter', 'testbench', tb, 0)

if 'SYS-110.tbc' in testbenches:
    checkbutton_1.select()
if 'SYS-112.tbc' in testbenches:
    checkbutton_2.select()

# Loop for waiting for interaction of the user
window.mainloop()
