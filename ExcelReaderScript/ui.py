import tkinter as tk
from evaluate_excel import calculate_results, save_filter, read_filter_json

window = tk.Tk()
# Create title of the window
window.title('Test Result Calculator')
# Set size of the window
window.minsize(width=450, height=200)

# Label for testbenches to be included
tb_label = tk.Label(text='Testbenches to include',
                    font=('Arial', 8, 'bold'))
tb_label.grid(column=0, row=0, padx=20, pady=5)


# Checkbuttons for testbenches
def checkbutton_1_used():
    json_file_path = json_file_input.get()
    state = checked_state_1.get()
    save_filter(json_file_path, 'result_filter', 'testbench', 'SYS-110.tbc',
                state)


def checkbutton_2_used():
    json_file_path = json_file_input.get()
    state = checked_state_2.get()
    save_filter(json_file_path, 'result_filter', 'testbench', 'SYS-112.tbc',
                state)


def checkbutton_3_used():
    json_file_path = json_file_input.get()
    tb_input = input_field.get()
    tb_name = tb_input + '.tbc'
    if tb_input:
        state = checked_state_3.get()
        save_filter(json_file_path, 'result_filter', 'testbench', tb_name,
                    state)
    else:
        checkbutton_3.deselect()
        print("No input given.")


# Checkbutton SYS-110
checked_state_1 = tk.IntVar()
checkbutton_1 = tk.Checkbutton(text='SYS-110',
                               variable=checked_state_1,
                               command=checkbutton_1_used)
checkbutton_1.grid(column=0, row=1, sticky='w', padx=20, pady=5)

# Checkbutton SYS-112
checked_state_2 = tk.IntVar()
checkbutton_2 = tk.Checkbutton(text='SYS-112',
                               variable=checked_state_2,
                               command=checkbutton_2_used)
checkbutton_2.grid(column=0, row=2, sticky='w', padx=20, pady=5)

# Entry for additional testbench
checked_state_3 = tk.IntVar()
checkbutton_3 = tk.Checkbutton(text='Other:   ',
                               variable=checked_state_3,
                               command=checkbutton_3_used)
checkbutton_3.grid(column=0, row=3, sticky='w', padx=20)
input_field = tk.Entry(width=10)
input_field.grid(column=0, row=4, sticky='nw', padx=25)


# Label for json file path
json_file_label = tk.Label(text='Load filter data from:',
                           font=('Arial', 8, 'bold'))
json_file_label.grid(column=1, row=0, sticky='w')

# Input line for file path
json_file_input = tk.Entry(width=40)
json_file_input.insert(0, 'filter.json')
json_file_input.grid(column=1, row=1, columnspan=2, sticky='w')

# Label for target location for the report
report_excel_label = tk.Label(text='Save report excel in:',
                              font=('Arial', 8, 'bold'))
report_excel_label.grid(column=1, row=2, sticky='w')

# Input line for location of the report excel
loc_report_excel = tk.Entry(width=40)
loc_report_excel.grid(column=1, row=3, columnspan=2, sticky='w')


# Start button
def start_button_clicked():
    json_file_path = json_file_input.get()
    filter_data = read_filter_json(json_file_path)
    calculate_results(filter_data)
    print('Calculation finished')


start_button = tk.Button(text="Calculate", command=start_button_clicked)
start_button.grid(column=2, row=4, sticky='e', pady=20)

# Set default settings on the UI
# Remove all testbenches except the default testbenches from the json file
json_file_path = json_file_input.get()
default = read_filter_json(json_file_path)
testbenches = default['result_filter']['testbench']
for tb in testbenches:
    if tb not in ['SYS-110.tbc', 'SYS-112.tbc']:
        save_filter(json_file_path, 'result_filter', 'testbench', tb, 0)
# Activate checkboxes of the default testbenches if they are in the json dict
if 'SYS-110.tbc' in testbenches:
    checkbutton_1.select()
if 'SYS-112.tbc' in testbenches:
    checkbutton_2.select()

# Loop for waiting for interaction of the user
window.mainloop()
