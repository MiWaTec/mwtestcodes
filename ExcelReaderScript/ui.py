import tkinter as tk
from tkinter import filedialog
import json
from evaluate_excel import calculate_results, save_filter, read_filter_json,\
                           save_default_settings, write_results_in_template,\
                           dataframe_to_excel


class ButtonCreator:
    _instances = []
    _counter = 1

    def __init__(self, name) -> None:
        self.name = name
        self.setting_button = tk.Button(page1, text=self.name,
                                        command=self.setting_button_used,
                                        width=20, height=2)
        self.setting_button.grid(column=1, row=ButtonCreator._counter,
                                 padx=5, pady=5)
        ButtonCreator._counter += 1
        ButtonCreator._instances.append(self)

    def setting_button_used(self):
        page3.tkraise()
        load_settings(self.name)

    def get_all_instances() -> list:
        """This function returns a list of all created instances of the class.

        Returns:
            list: A list of all instances of the class that were instantiated.
        """
        return ButtonCreator._instances

    def delete_button(self: object):
        """This function deletes the given class object.

        Args:
            self (object): Instance of the class that will be deleted.
        """
        self.setting_button.destroy()


class CheckboxCreator:
    _instances = []
    _counter = 0

    def __init__(self, name) -> None:
        self.name = name
        self.checked_state = tk.IntVar()
        self.checkbutton = tk.Checkbutton(page3, text=self.name[:-4],
                                          variable=self.checked_state,
                                          command=self.checkbutton_used)
        self.checkbutton.grid(column=0, row=CheckboxCreator._counter+4,
                              sticky='nw', columnspan=2, padx=5, pady=5)
        CheckboxCreator._counter += 1
        CheckboxCreator._instances.append(self)
        for obj in CheckboxCreator._instances:
            print(obj.name)
        print('end')
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
        save_filter(json_file_path, 'result_filter', 'tbc',
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
    setting_name = setting_label.cget('text')
    tb_name = input_tb.get() + '.tbc'
    if tb_name:
        default_data = read_filter_json('default_settings.json')
        tb_list = default_data[setting_name]['testbenches']
        if tb_name not in tb_list:
            tb_list.append(tb_name)
            save_default_settings('default_settings.json', setting_name,
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
    setting_name = setting_label.cget('text')
    tb_name = input_tb.get() + '.tbc'
    default_data = read_filter_json('default_settings.json')
    tb_list = default_data[setting_name]['testbenches']
    if tb_name in tb_list:
        checkbox_list = CheckboxCreator.get_all_instances()
        for checkbox in checkbox_list:
            if checkbox.name == tb_name:
                CheckboxCreator.delete_checkbox(checkbox)
                break
        tb_list.remove(tb_name)
        save_default_settings('default_settings.json', setting_name,
                              'testbenches', tb_list)
        save_filter(default_data[setting_name]['json_file'], 'result_filter',
                    'tbc', tb_name, 0)
    else:
        print('No valid input given.')


def browse_file(input_field, default_setting):
    """This finction will be executed if the 'Browse' of the
       'Load filter file' entry was pressed. It will open a window
       from which the file can be chosen.
    """
    file_path = filedialog.askopenfilename()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, file_path)
    save_default_settings('default_settings.json',
                          default_setting, file_path)


def browse_folder(input_field, default_setting):
    """This finction will be executed if the 'Browse' of the
       'Save report excel in' entry was pressed. It will open a window
       from which the folder can be chosen.
    """
    destination_folder = filedialog.askdirectory()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, destination_folder)
    save_default_settings('default_settings.json',
                          default_setting, destination_folder)


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


def load_settings(setting):
    # Set the setting name
    setting_label.config(text=setting)
    # Load default data dict
    default = read_filter_json('default_settings.json')
    # Set default json file path
    json_file_input.insert(0, default[setting]['json_file'])
    # Set default nightly results folder
    nightlyres_input.insert(0, default[setting]['results_folder'])
    # Set template file
    template_excel.insert(0, default[setting]['template_file'])
    # Set folder for the report excel
    loc_report_excel.insert(0, default[setting]['location_report'])
    # Set report file name
    report_file_name.insert(0, default[setting]['report_name'])
    # Load checkbuttons of default testbenches
    for default_tb in default[setting]['testbenches']:
        CheckboxCreator(default_tb)
    # Remove all testbenches except the default testbenches from the json file
    json_file_path = json_file_input.get()
    if json_file_path == '':
        return None
    filter_json = read_filter_json(json_file_path)
    testbenches = filter_json['result_filter']['tbc']
    for tb in testbenches:
        if tb not in default[setting]['testbenches']:
            save_filter(json_file_path, 'result_filter', 'tbc', tb, 0)
    # Activate checkboxes of the default tbs if they are in the json dict
    checkbox_list = CheckboxCreator.get_all_instances()
    for checkbox in checkbox_list:
        if checkbox.name in testbenches:
            checkbox.checkbutton.select()
    print(checkbox_list)


def unload_settings():
    # Remove default json file path
    json_file_input.delete(0, tk.END)
    # Remove default nightly results folder
    nightlyres_input.delete(0, tk.END)
    # Remove template file
    template_excel.delete(0, tk.END)
    # Remove folder for the report excel
    loc_report_excel.delete(0, tk.END)
    # Remove report file name
    report_file_name.delete(0, tk.END)
    # Remove testbenches
    checkbox_list = CheckboxCreator.get_all_instances()
    CheckboxCreator._counter = 0
    for checkbox in checkbox_list:
        CheckboxCreator.delete_checkbox(checkbox)


def load_available_settings(default_json_file):
    settings_dict = read_filter_json(default_json_file)
    for setting in settings_dict:
        ButtonCreator(setting)


def create_setting():
    page2.tkraise()


def set_new_setting(setting_name: str):
    """This function adds a new setting to the default_settings.json and opens
       the new created setting in the UI.

    Args:
        setting_name (str): _description_
    """
    default_dict = {
        'json_file': '',
        'results_folder': '',
        'template_file': '',
        'location_report': '',
        'report_name': '',
        'testbenches': []
    }
    # Add a new settings dict to the defaul_settings.json file
    settings_dict = read_filter_json('default_settings.json')
    settings_dict[setting_name] = default_dict
    with open('default_settings.json', 'w') as f:
        json.dump(settings_dict, f, indent=4)
    # Open the new created setting
    unload_settings()
    load_settings(setting_name)
    page3.tkraise()


def unload_available_settings():
    btn_list = ButtonCreator.get_all_instances()
    for btn in btn_list:
        ButtonCreator.delete_button(btn)
    ButtonCreator._counter = 1


def remove_setting(setting: str):
    """This function deletes the given setting from the default_settings.json
       and from the UI main page.

    Args:
        setting (str): Name of the setting that will be removed.
    """
    settings_dict = read_filter_json('default_settings.json')
    del settings_dict[setting]
    with open('default_settings.json', 'w') as f:
        json.dump(settings_dict, f, indent=4)
    unload_available_settings()
    load_available_settings('default_settings.json')


def menubar_go_to_mainmenu():
    unload_settings()
    unload_available_settings()
    load_available_settings('default_settings.json')
    page1.tkraise()


def menubar_go_to_setup():
    page4.tkraise()


# Create UI window
window = tk.Tk()
# Create title of the window
window.title('Test Result Calculator')
# Set size of the window
window.minsize(width=555, height=200)
window.resizable(False, False)


# Create Menubar
menubar = tk.Menu(window)
window.config(menu=menubar)
# File Menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Main', menu=file_menu)
file_menu.add_command(label='Main menu', command=menubar_go_to_mainmenu)
# Setup
setup_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Setup', menu=setup_menu)
setup_menu.add_command(label='Configurate filter', command=menubar_go_to_setup)


# Page 1
page1 = tk.Frame(window)
page1.grid(row=0, column=0, sticky='nsew')

# Label for available settings
available_set = tk.Label(page1, text='Available settings:',
                         font=('Arial', 14, 'bold'))
available_set.grid(row=0, column=0, padx=10, pady=5)
# Button for creating a new setting
btn_new_setting = tk.Button(page1, text='Create new setting', width=16,
                            height=1, command=lambda:
                            create_setting())
btn_new_setting.grid(column=0, row=1, sticky='we', padx=10, pady=5)
# Button for removing an existing setting
btn_create_new_setting = tk.Button(page1, text='Remove setting', width=16,
                                   height=1, command=lambda:
                                   remove_setting(input_del_setting.get()))
btn_create_new_setting.grid(column=0, row=2, sticky='we', padx=10, pady=5)
input_del_setting = tk.Entry(page1, width=16)
input_del_setting.grid(column=0, row=3, sticky='we', padx=10, pady=5)


# Page 2
page2 = tk.Frame(window)
page2.grid(row=0, column=0, sticky='nsew')
page2.columnconfigure((0, 1, 2), weight=1)
page2.rowconfigure((0, 1, 2, 3), weight=1)

# Label for creating a new setting
new_setting_label = tk.Label(page2, text='Enter a name for the new setting:',
                             font=('Arial', 14, 'bold'))
new_setting_label.grid(column=1, row=1, sticky='n')

# Input line for the name of the new setting
input_name_new_setting = tk.Entry(page2, width=38)
input_name_new_setting.grid(column=1, row=2, sticky='n')

# Button for setting up the new setting
btn_set_new_setting = tk.Button(page2, text='Create', width=32, command=lambda:
                                set_new_setting(input_name_new_setting.get()))
btn_set_new_setting.grid(column=1, row=3, sticky='n')


# Page 3
page3 = tk.Frame(window)
page3.grid(row=0, column=0, sticky='nsew')

# Label for name of the setting
setting_label = tk.Label(page3, text='',
                         font=('Arial', 8, 'bold'))
setting_label.grid(column=0, row=0, columnspan=2, sticky='w', padx=10, pady=5)

# Label for testbenches to be included
tb_label = tk.Label(page3, text='Testbenches',
                    font=('Arial', 8, 'bold'))
tb_label.grid(column=0, row=1, columnspan=2, sticky='w', padx=10, pady=5)

# Input field for testbenches
input_tb = tk.Entry(page3, width=16)
input_tb.grid(column=0, row=2, columnspan=2, sticky='nw', padx=10)

# Add button for testbenches
btn_tb_add = tk.Button(page3, text='Add', width=5, command=btn_tb_add_clicked)
btn_tb_add.grid(column=0, row=3, sticky='e', padx=5, pady=5)

# Delete button for testbenches
btn_tb_del = tk.Button(page3, text='Delete', width=5,
                       command=btn_tb_del_clicked)
btn_tb_del.grid(column=1, row=3, sticky='w', padx=5, pady=5)

# Label for json file path
json_file_label = tk.Label(page3, text='Load filter file:',
                           font=('Arial', 8, 'bold'))
json_file_label.grid(column=2, row=1, sticky='w')

# Input line for json file path
json_file_input = tk.Entry(page3, width=60)
json_file_input.grid(column=2, row=2, columnspan=2, sticky='w')
btn_browse_filter = tk.Button(page3, text='Browse', width=7,
                              command=lambda: browse_file(json_file_input,
                                                          'json_file'))
btn_browse_filter.grid(column=4, row=2, sticky='w')

# Label for folder with excel files
excel_folder_label = tk.Label(page3, text='Folder with nightly results',
                              font=('Arial', 8, 'bold'))
excel_folder_label.grid(column=2, row=3, sticky='w')

# Input line for folder path with nightly results
nightlyres_input = tk.Entry(page3, width=60)
nightlyres_input.grid(column=2, row=4, columnspan=2, sticky='w')
btn_browse_results = tk.Button(page3, text='Browse', width=7,
                               command=lambda: browse_folder(nightlyres_input,
                                                             'results_folder'))
btn_browse_results.grid(column=4, row=4, sticky='w')

# Label for template to be used
report_excel_label = tk.Label(page3, text='Load template file:',
                              font=('Arial', 8, 'bold'))
report_excel_label.grid(column=2, row=5, sticky='w')

# Input line for template to be used
template_excel = tk.Entry(page3, width=60)
template_excel.grid(column=2, row=6, columnspan=2, sticky='n', pady=2)
btn_browse_template = tk.Button(page3, text='Browse', width=7,
                                command=lambda: browse_file(template_excel,
                                                            'template_file'))
btn_browse_template.grid(column=4, row=6, sticky='n')

# Label for target location for the report
report_excel_label = tk.Label(page3, text='Save report excel in:',
                              font=('Arial', 8, 'bold'))
report_excel_label.grid(column=2, row=7, sticky='w')

# Input line for location of the report excel
loc_report_excel = tk.Entry(page3, width=60)
loc_report_excel.grid(column=2, row=8, columnspan=2, sticky='n', pady=2)
btn_browse_folder = tk.Button(page3, text='Browse', width=7,
                              command=lambda: browse_folder(loc_report_excel,
                                                            'location_report'))
btn_browse_folder.grid(column=4, row=8, sticky='n')

# Label for name of the report file
report_file_name_label = tk.Label(page3, text='Report file name',
                                  font=('Arial', 8, 'bold'))
report_file_name_label.grid(column=2, row=9, sticky='w')

# Input line for the name of the report file
report_file_name = tk.Entry(page3, width=60)
report_file_name.grid(column=2, row=10, columnspan=2, sticky='n')

# Start button
start_button = tk.Button(page3, text='Calculate', width=7,
                         command=start_button_clicked)
start_button.grid(column=4, row=11, sticky='e', pady=10)


# Page 4
page4 = tk.Frame(window)
page4.grid(row=0, column=0, sticky='nsew')

# Label for title of creating a filter
title_frame = tk.Frame(page4, bd=1, relief='raised')
title_frame.grid(row=0, column=0, sticky='nsew', padx=10)
filter_label = tk.Label(title_frame, text='Configurate filter',
                        font=('Arial', 14, 'bold'))
filter_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)

# Page 4 / Frame for filter
filter_frame = tk.LabelFrame(page4, text='Filter', bd=2, relief='ridge')
filter_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=5)

# Label for sideheader
sideheader_label = tk.Label(filter_frame, text='Sideheader',
                            font=('Arial', 8, 'bold'))
sideheader_label.grid(column=0, row=1, padx=10)

# Label for header
header_label = tk.Label(filter_frame, text='Header',
                        font=('Arial', 8, 'bold'))
header_label.grid(column=1, row=1, padx=10)

# Label for value to be calculated
calculate_value_label = tk.Label(filter_frame, text='Calculate value',
                                 font=('Arial', 8, 'bold'))
calculate_value_label.grid(column=2, row=1, padx=10)

# Label for testcases
testcases_label = tk.Label(filter_frame, text='Testcases',
                           font=('Arial', 8, 'bold'))
testcases_label.grid(column=3, row=1, padx=10)

# Label for variables
variables_label = tk.Label(filter_frame, text='Variables',
                           font=('Arial', 8, 'bold'))
variables_label.grid(column=4, row=1, padx=10)

# Display page 1
page1.tkraise()
load_available_settings('default_settings.json')

# Loop for waiting for interaction of the user
window.mainloop()
