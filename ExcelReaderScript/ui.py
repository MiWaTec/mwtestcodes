import tkinter as tk
import json
from evaluate_excel import calculate_results, save_filter

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
if 'SYS-110.tbc' in testbenches:
    checkbutton_1.select()
if 'SYS-112.tbc' in testbenches:
    checkbutton_2.select()

# Loop for waiting for interaction of the user
window.mainloop()
