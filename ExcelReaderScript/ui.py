import tkinter as tk
from evaluate_excel import calculate_results, save_filter, read_filter_json,\
                           save_default_settings, write_results_in_template,\
                           dataframe_to_excel


class CheckboxCreator:
    _instances = []
    _counter = 3

    def __init__(self, name) -> None:
        self.name = name
        self.checked_state = tk.IntVar()
        self.checkbutton = tk.Checkbutton(text=name,
                                          variable=self.checked_state,
                                          command=self.checkbutton_used)
        self.checkbutton.grid(column=0, row=CheckboxCreator._counter,
                              sticky='nw', columnspan=2, padx=5, pady=5)
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
        """This function will be executed after a testbench checkbox of the
           UI was clicked. The state of the checkbox will be saved in the
           filter data json file. If the state is deactivated, the testbench
           will be removed from the filter file. If the state is activated, the
           testbench name will be added in the filter file.
        """
        json_file_path = json_file_input.get()
        state = self.checked_state.get()
        save_filter(json_file_path, 'result_filter', 'testbench',
                    self.name, state)

    def get_all_instances() -> list:
        """This function returns a list of all created instances of the class.

        Returns:
            list: A list of all instances of the class that were instantiated.
        """
        return CheckboxCreator._instances

    def delete_checkbox(self: object):
        """This function deletes the given class object.

        Args:
            self (object): Instance of the class that will be deleted.
        """
        self.checkbutton.destroy()


def btn_tb_add_clicked():
    """This function will be executed after the 'Add' button of the
       UI was clicked. A new checkbox will be created in the UI with
       the name which was provided through the input field. If a
       checkbox with the same name already exists or no input was
       given in the input field, no new checkbox will be created.
    """
    tb_name = input_tb.get() + '.tbc'
    if tb_name:
        default_data = read_filter_json('default_settings.json')
        tb_list = default_data['testbenches']
        if tb_name not in tb_list:
            tb_list.append(tb_name)
            save_default_settings('default_settings.json',
                                  'testbenches', tb_list)
            CheckboxCreator(tb_name)
            print('Testbench added.')
        else:
            print('Testbench already exists.')
    else:
        print('No input given.')


def btn_tb_del_clicked():
    """This function will be executed after the 'Delete' button of the
       UI was clicked. The checkbox with the name which was given through
       the input field will be deleted.
    """
    tb_name = input_tb.get() + '.tbc'
    default_data = read_filter_json('default_settings.json')
    tb_list = default_data['testbenches']
    if tb_name in tb_list:
        checkbox_list = CheckboxCreator.get_all_instances()
        for checkbox in checkbox_list:
            if checkbox.name == tb_name:
                CheckboxCreator.delete_checkbox(checkbox)
                break
        tb_list.remove(tb_name)
        save_default_settings('default_settings.json', 'testbenches', tb_list)
        save_filter(default_data['json_file'], 'result_filter', 'testbench',
                    tb_name, 0)
    else:
        print('No valid input given.')


def start_button_clicked():
    """This function will be executed after the 'Start' button of the
       UI was clicked. The calculation of the desired values based on the
       filter data of the filter json file will be started.
    """
    json_file_path = json_file_input.get()
    filter_data = read_filter_json(json_file_path)
    res = calculate_results(filter_data)
    df = write_results_in_template('EvaluationExcel.xlsx', res)
    dataframe_to_excel(df)


window = tk.Tk()
# Create title of the window
window.title('Test Result Calculator')
# Set size of the window
window.minsize(width=400, height=200)

# Label for testbenches to be included
tb_label = tk.Label(text='Testbenches',
                    font=('Arial', 8, 'bold'))
tb_label.grid(column=0, row=0, columnspan=2, sticky='w', padx=10, pady=5)

# Input field for testbenches
input_tb = tk.Entry(width=16)
input_tb.grid(column=0, row=1, columnspan=2, sticky='nw', padx=10)

# Add button for testbenches
btn_tb_add = tk.Button(text="Add", width=5, command=btn_tb_add_clicked)
btn_tb_add.grid(column=0, row=2, sticky='e', padx=5, pady=5)

# Delete button for testbenches
btn_tb_del = tk.Button(text="Delete", width=5, command=btn_tb_del_clicked)
btn_tb_del.grid(column=1, row=2, sticky='w', padx=5, pady=5)

# Label for json file path
json_file_label = tk.Label(text='Load filter data from:',
                           font=('Arial', 8, 'bold'))
json_file_label.grid(column=2, row=0, sticky='w')

# Input line for file path
json_file_input = tk.Entry(width=40)
json_file_input.grid(column=2, row=1, columnspan=2, sticky='w')

# Label for target location for the report
report_excel_label = tk.Label(text='Save report excel in:',
                              font=('Arial', 8, 'bold'))
report_excel_label.grid(column=2, row=2, sticky='w')

# Input line for location of the report excel
loc_report_excel = tk.Entry(width=40)
loc_report_excel.grid(column=2, row=3, columnspan=2, sticky='w')

# Start button
start_button = tk.Button(text="Calculate", command=start_button_clicked)
start_button.grid(column=3, row=4, sticky='e', pady=5)


# Set default settings on the UI when starting the program

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
checkbox_list = CheckboxCreator.get_all_instances()
for checkbox in checkbox_list:
    if checkbox.name in testbenches:
        checkbox.checkbutton.select()
print(checkbox_list)

# Loop for waiting for interaction of the user
window.mainloop()
