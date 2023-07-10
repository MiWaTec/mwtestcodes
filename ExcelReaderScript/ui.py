import tkinter as tk
from tkinter import filedialog
from evaluate_excel import calculate_results, save_filter, read_filter_json,\
                           save_default_settings, write_results_in_template,\
                           dataframe_to_excel


class CheckboxCreator:
    _instances = []
    _counter = 3

    def __init__(self, name) -> None:
        self.name = name
        self.checked_state = tk.IntVar()
        self.checkbutton = tk.Checkbutton(text=self.name[:-4],
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


def browse_file(input_field):
    """This finction will be executed if the 'Browse' of the
       'Load filter file' entry was pressed. It will open a window
       from which the file can be chosen.
    """
    file_path = filedialog.askopenfilename()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, file_path)


def browse_folder(input_field):
    """This finction will be executed if the 'Browse' of the
       'Save report excel in' entry was pressed. It will open a window
       from which the folder can be chosen.
    """
    destination_folder = filedialog.askdirectory()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, destination_folder)


def start_button_clicked():
    """This function will be executed after the 'Start' button of the
       UI was clicked. The calculation of the desired values based on the
       filter data of the filter json file will be started.
    """
    json_file_path = json_file_input.get()
    filter_data = read_filter_json(json_file_path)
    nightly_excels = nightlyres_input.get()
    res = calculate_results(filter_data, nightly_excels)
    template_file = template_excel.get()
    df = write_results_in_template(template_file, res)
    report_excel_folder = loc_report_excel.get()
    report_excel_name = report_file_name.get()
    dataframe_to_excel(df, report_excel_folder, report_excel_name)


window = tk.Tk()
# Create title of the window
window.title('Test Result Calculator')
# Set size of the window
window.minsize(width=555, height=200)

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
json_file_label = tk.Label(text='Load filter file:',
                           font=('Arial', 8, 'bold'))
json_file_label.grid(column=2, row=0, sticky='w')

# Input line for json file path
json_file_input = tk.Entry(width=60)
json_file_input.grid(column=2, row=1, columnspan=2, sticky='w')
btn_browse_filter = tk.Button(text="Browse", width=7,
                              command=lambda: browse_file(json_file_input))
btn_browse_filter.grid(column=4, row=1, sticky='w')

# Label for folder with excel files
excel_folder_label = tk.Label(text='Folder with nightly results',
                              font=('Arial', 8, 'bold'))
excel_folder_label.grid(column=2, row=2, sticky='w')

# Input line for folder path with nightly results
nightlyres_input = tk.Entry(width=60)
nightlyres_input.grid(column=2, row=3, columnspan=2, sticky='w')
btn_browse_results = tk.Button(text="Browse", width=7,
                               command=lambda: browse_folder(nightlyres_input))
btn_browse_results.grid(column=4, row=3, sticky='w')

# Label for template to be used
report_excel_label = tk.Label(text='Load template file:',
                              font=('Arial', 8, 'bold'))
report_excel_label.grid(column=2, row=4, sticky='w')

# Input line for template to be used
template_excel = tk.Entry(width=60)
template_excel.grid(column=2, row=5, columnspan=2, sticky='n', pady=2)
btn_browse_template = tk.Button(text="Browse", width=7,
                                command=lambda: browse_file(template_excel))
btn_browse_template.grid(column=4, row=5, sticky='n')

# Label for target location for the report
report_excel_label = tk.Label(text='Save report excel in:',
                              font=('Arial', 8, 'bold'))
report_excel_label.grid(column=2, row=6, sticky='w')

# Input line for location of the report excel
loc_report_excel = tk.Entry(width=60)
loc_report_excel.grid(column=2, row=7, columnspan=2, sticky='n', pady=2)
btn_browse_folder = tk.Button(text="Browse", width=7,
                              command=lambda: browse_folder(loc_report_excel))
btn_browse_folder.grid(column=4, row=7, sticky='n')

# Label for name of the report file
report_file_name_label = tk.Label(text='Report file name',
                                  font=('Arial', 8, 'bold'))
report_file_name_label.grid(column=2, row=8, sticky='w')

# Input line for the name of the report file
report_file_name = tk.Entry(width=60)
report_file_name.grid(column=2, row=9, columnspan=2, sticky='n')

# Start button
start_button = tk.Button(text="Calculate", width=7,
                         command=start_button_clicked)
start_button.grid(column=4, row=10, sticky='e', pady=10)


# Set default settings on the UI when starting the program

# Load default data dict
default = read_filter_json('default_settings.json')
# Set default json file path
json_file_input.insert(0, default['json_file'])
# Set default nightly results folder
nightlyres_input.insert(0, default['nightly_results_folder'])
# Set template file
template_excel.insert(0, default['template_file'])
# Set folder for the report excel
loc_report_excel.insert(0, default['location_report'])
# Set report file name
report_file_name.insert(0, default['report_name'])
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
