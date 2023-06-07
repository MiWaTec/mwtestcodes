import tkinter as tk
from evaluate_excel import calculate_results, save_filter, read_filter_json, save_default_settings


class CheckboxCreator:
    _instances = []
    _counter = 4

    def __init__(self, name) -> None:
        self.name = name
        self.checked_state = tk.IntVar()
        self.checkbutton = tk.Checkbutton(text=name,
                                          variable=self.checked_state,
                                          command=self.checkbutton_used)
        self.checkbutton.grid(column=0, row=CheckboxCreator._counter,
                              sticky='nw', padx=20, pady=5)
        CheckboxCreator._counter += 1
        CheckboxCreator._instances.append(self)
        for obj in CheckboxCreator._instances:
            print(obj.name)
        print("end")
        print(self.name)
        print(CheckboxCreator._counter)
        print(self.checked_state.get())
        print(CheckboxCreator._instances)
        print(len(CheckboxCreator._instances))

    def checkbutton_used(self):
        json_file_path = json_file_input.get()
        state = self.checked_state.get()
        save_filter(json_file_path, 'result_filter', 'testbench',
                    self.name, state)
        print("class executed")

    def get_all_instances():
        return CheckboxCreator._instances



def btn_tb_add_clicked():
    tb_name = input_tb.get() + '.tbc'
    print(input_tb)
    if tb_name:
        setting_changed = save_default_settings('default_settings.json',
                                                'testbenches', tb_name)
        if setting_changed:
            CheckboxCreator(tb_name)
            print('Testbench added.')
        else:
            print('Testbench already exists.')
    else:
        print('No input given.')


def btn_tb_del_clicked():
    tb_name = input_tb.get()
    print(input_tb)
    if tb_name:
        save_default_settings('default_settings.json', 'testbenches', tb_name)
    else:
        print('No input given.')


def start_button_clicked():
    json_file_path = json_file_input.get()
    filter_data = read_filter_json(json_file_path)
    calculate_results(filter_data)
    print('Calculation finished')


window = tk.Tk()
# Create title of the window
window.title('Test Result Calculator')
# Set size of the window
window.minsize(width=450, height=200)

# Label for testbenches to be included
tb_label = tk.Label(text='Testbenches',
                    font=('Arial', 8, 'bold'))
tb_label.grid(column=0, row=0, padx=20, pady=5)

# Input field for testbenches
input_tb = tk.Entry(width=13)
input_tb.grid(column=0, row=1, sticky='nw', padx=20)

# Add button for testbenches
btn_tb_add = tk.Button(text="Add", width=10, command=btn_tb_add_clicked)
btn_tb_add.grid(column=0, row=2, sticky='nw', padx=20, pady=5)

# Delete button
btn_tb_del = tk.Button(text="Del", width=10, command=btn_tb_del_clicked)
btn_tb_del.grid(column=0, row=3, sticky='nw', padx=20, pady=5)

# Label for json file path
json_file_label = tk.Label(text='Load filter data from:',
                           font=('Arial', 8, 'bold'))
json_file_label.grid(column=1, row=0, sticky='w')

# Input line for file path
json_file_input = tk.Entry(width=40)
json_file_input.grid(column=1, row=1, columnspan=2, sticky='w')

# Label for target location for the report
report_excel_label = tk.Label(text='Save report excel in:',
                              font=('Arial', 8, 'bold'))
report_excel_label.grid(column=1, row=2, sticky='w')

# Input line for location of the report excel
loc_report_excel = tk.Entry(width=40)
loc_report_excel.grid(column=1, row=3, columnspan=2, sticky='w')


# Start button
start_button = tk.Button(text="Calculate", command=start_button_clicked)
start_button.grid(column=2, row=4, sticky='e', pady=5)

# Set default settings on the UI
# Load default data dict
default = read_filter_json('default_settings.json')
# Set default json file path
json_file_input.insert(0, default['json_file'])
# Load checkbuttons of default testbenches
for default_tb in default['testbenches']:
    CheckboxCreator(default_tb)
# Remove all testbenches except the default testbenches from the json file
json_file_path = json_file_input.get()
filter_json = read_filter_json(json_file_path)
testbenches = filter_json['result_filter']['testbench']
for tb in testbenches:
    if tb not in default['testbenches']:
        save_filter(json_file_path, 'result_filter', 'testbench', tb, 0)
# Activate checkboxes of the default testbenches if they are in the json dict
# if 'SYS-110.tbc' in testbenches:
#     checkbutton_1.select()
# if 'SYS-112.tbc' in testbenches:
#     checkbutton_2.select()
print("Y")
checkbox_list = CheckboxCreator.get_all_instances()
for checkbox in checkbox_list:
    if checkbox.name in testbenches:
        checkbox.checkbutton.select()
print(checkbox_list)
# Loop for waiting for interaction of the user
window.mainloop()
