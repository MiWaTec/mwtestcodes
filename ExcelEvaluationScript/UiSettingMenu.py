import tkinter as tk
from tkinter import filedialog
import UiElementCreator
from evaluate_excel import read_filter_json, save_filter,\
                           save_default_settings, calculate_results,\
                           write_results_in_template,\
                           dataframe_to_excel

testbenches_frame = None
setting_label = None
json_file_input = None
nightlyres_input = None
template_excel = None
row_number_headers = None
loc_report_excel = None
report_file_name = None
input_tb = None


def initialize_page_setting(window):
    # Page setting
    page3 = tk.Frame(window)
    page3.grid(row=0, column=0, sticky='nsew')

    # Frame for name of the setting
    setting_name_frame = tk.Frame(page3, bd=1, relief='raised')
    setting_name_frame.grid(column=0, row=0, columnspan=2, sticky='nsew',
                            padx=10, pady=5)

    # Label for name of the setting
    global setting_label
    setting_label = tk.Label(setting_name_frame, text='',
                             font=('Arial', 8, 'bold'))
    setting_label.grid(column=0, row=0, columnspan=2, sticky='w', padx=10,
                       pady=5)

    # Label for testbenches to be included
    tb_label = tk.Label(page3, text='Testbenches',
                        font=('Arial', 8, 'bold'))
    tb_label.grid(column=0, row=1, columnspan=2, sticky='w', padx=10, pady=5)

    # Frame for adding and deleting testbenches
    global testbenches_frame
    testbenches_frame = tk.LabelFrame(page3, text='Testbenches', bd=2,
                                      relief='ridge')
    testbenches_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=5)

    # Input field for testbenches
    global input_tb
    input_tb = tk.Entry(testbenches_frame, width=16)
    input_tb.grid(column=0, row=2, columnspan=2, sticky='nw', padx=10)

    # Add button for testbenches
    btn_tb_add = tk.Button(testbenches_frame, text='Add', width=5,
                           command=lambda: btn_tb_add_clicked(json_file_input.get()))
    btn_tb_add.grid(column=0, row=3, sticky='e', padx=5, pady=5)

    # Delete button for testbenches
    btn_tb_del = tk.Button(testbenches_frame, text='Delete', width=5,
                           command=btn_tb_del_clicked)
    btn_tb_del.grid(column=1, row=3, sticky='w', padx=5, pady=5)

    # Page 3 / Frame for configurations
    config_frame = tk.LabelFrame(page3, text='Configuration', bd=2,
                                 relief='ridge', height=150, width=200)
    config_frame.grid(row=1, column=1, sticky='nsew', padx=10, pady=5)

    # Label for json file path
    json_file_label = tk.Label(config_frame, text='Load filter file:',
                               font=('Arial', 8, 'bold'))
    json_file_label.grid(column=2, row=1, sticky='w')

    # Input line for json file path
    global json_file_input
    json_file_input = tk.Entry(config_frame, width=120)
    json_file_input.grid(column=2, row=2, columnspan=2, sticky='w', padx=5,
                         pady=5)
    btn_browse_filter = tk.Button(config_frame, text='Browse', width=7,
                                  command=lambda:
                                  browse_file(json_file_input,
                                              setting_label.cget('text'),
                                              'json_file'))
    btn_browse_filter.grid(column=4, row=2, sticky='w')

    # Label for folder with excel files
    excel_folder_label = tk.Label(config_frame,
                                  text='Folder with nightly results',
                                  font=('Arial', 8, 'bold'))
    excel_folder_label.grid(column=2, row=3, sticky='w')

    # Input line for folder path with nightly results
    global nightlyres_input
    nightlyres_input = tk.Entry(config_frame, width=120)
    nightlyres_input.grid(column=2, row=4, columnspan=2, sticky='w', padx=5,
                          pady=5)
    btn_browse_results = tk.Button(config_frame, text='Browse', width=7,
                                   command=lambda:
                                   browse_folder(nightlyres_input,
                                                 setting_label.cget('text'),
                                                 'results_folder'))
    btn_browse_results.grid(column=4, row=4, sticky='w')

    # Label for template to be used
    template_label = tk.Label(config_frame, text='Load template file:',
                              font=('Arial', 8, 'bold'))
    template_label.grid(column=2, row=5, sticky='w')

    # Input line for template to be used
    global template_excel
    template_excel = tk.Entry(config_frame, width=120)
    template_excel.grid(column=2, row=6, columnspan=2, sticky='n', pady=2)
    btn_browse_template = tk.Button(config_frame, text='Browse', width=7,
                                    command=lambda:
                                    browse_file(template_excel,
                                                setting_label.cget('text'),
                                                'template_file'))
    btn_browse_template.grid(column=4, row=6, sticky='n')

    # Frame for row of the headers in template
    row_headers_frame = tk.Frame(config_frame, bd=1)
    row_headers_frame.grid(column=1, row=7, columnspan=2, sticky='nsew',
                           pady=5)
    # Label for template to be used
    row_headers_label = tk.Label(row_headers_frame,
                                 text='Row number of the headers:',
                                 font=('Arial', 8))
    row_headers_label.grid(column=0, row=0, sticky='w', padx=2)
    # Input line for row number of the headers
    global row_number_headers
    row_number_headers = tk.Entry(row_headers_frame, width=2)
    row_number_headers.grid(column=1, row=0, sticky='n', padx=5)

    # Label for target location for the report
    report_excel_label = tk.Label(config_frame, text='Save report excel in:',
                                  font=('Arial', 8, 'bold'))
    report_excel_label.grid(column=2, row=8, sticky='w')

    # Input line for location of the report excel
    global loc_report_excel
    loc_report_excel = tk.Entry(config_frame, width=120)
    loc_report_excel.grid(column=2, row=9, columnspan=2, sticky='n', pady=2)
    btn_browse_folder = tk.Button(config_frame, text='Browse', width=7,
                                  command=lambda:
                                  browse_folder(loc_report_excel,
                                                setting_label.cget('text'),
                                                'location_report'))
    btn_browse_folder.grid(column=4, row=9, sticky='n')

    # Label for name of the report file
    report_file_name_label = tk.Label(config_frame, text='Report file name',
                                      font=('Arial', 8, 'bold'))
    report_file_name_label.grid(column=2, row=10, sticky='w')

    # Input line for the name of the report file
    global report_file_name
    report_file_name = tk.Entry(config_frame, width=120)
    report_file_name.grid(column=2, row=11, columnspan=2, sticky='n',
                          pady=(0, 5))

    # Page 3 / Frame for start button
    start_btn_frame = tk.Frame(page3)
    start_btn_frame.grid(column=1, row=2, columnspan=2, sticky='nsew', padx=10,
                         pady=5)

    # Start button
    start_button = tk.Button(start_btn_frame, text='Calculate', width=7,
                             command=lambda:
                             [start_button_clicked(),
                              save_default_settings('default_settings.json',
                                                    setting_label.cget('text'),
                                                    'row_number_headers',
                                                    row_number_headers.get()),
                              save_default_settings('default_settings.json',
                                                    setting_label.cget('text'),
                                                    'report_name',
                                                    report_file_name.get())])
    start_button.grid(column=0, row=0, sticky='e', pady=(0, 5))


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
    # Set row number of the headers in template
    row_number_headers.insert(0, default[setting]['row_number_headers'])
    # Set folder for the report excel
    loc_report_excel.insert(0, default[setting]['location_report'])
    # Set report file name
    report_file_name.insert(0, default[setting]['report_name'])
    # Remove all testbenches except the default testbenches from the json file
    json_file_path = json_file_input.get()
    if json_file_path == '':
        return None
    filter_json = read_filter_json(json_file_path)
    testbenches = filter_json['result_filter']['tbc']
    for tb in testbenches:
        if tb not in default[setting]['testbenches']:
            save_filter(json_file_path, 'result_filter', 'tbc', tb, 0)
    # Load checkbuttons of default testbenches
    for default_tb in default[setting]['testbenches']:
        UiElementCreator.CheckboxCreator(default_tb, testbenches_frame,
                                         json_file_path)
    # Activate checkboxes of the default tbs if they are in the json dict
    checkbox_list = UiElementCreator.CheckboxCreator.get_all_instances()
    for checkbox in checkbox_list:
        if checkbox.name in testbenches:
            checkbox.checkbutton.select()


def unload_settings():
    # Break if previous settings not available
    if json_file_input is None:
        return None
    # Remove default json file path
    json_file_input.delete(0, tk.END)
    # Remove default nightly results folder
    nightlyres_input.delete(0, tk.END)
    # Remove template file
    template_excel.delete(0, tk.END)
    # Remove row number of headers in template
    row_number_headers.delete(0, tk.END)
    # Remove folder for the report excel
    loc_report_excel.delete(0, tk.END)
    # Remove report file name
    report_file_name.delete(0, tk.END)
    # Remove testbenches
    checkbox_list = UiElementCreator.CheckboxCreator.get_all_instances()
    for checkbox in checkbox_list:
        UiElementCreator.CheckboxCreator.delete_checkbox(checkbox)
    UiElementCreator.CheckboxCreator._counter = 0
    UiElementCreator.CheckboxCreator._instances = []


def btn_tb_add_clicked(json_file_path):
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
            UiElementCreator.CheckboxCreator(tb_name, testbenches_frame,
                                             json_file_path)
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
        checkbox_list = UiElementCreator.CheckboxCreator.get_all_instances()
        for checkbox in checkbox_list:
            if checkbox.name == tb_name:
                UiElementCreator.CheckboxCreator.delete_checkbox(checkbox)
                break
        tb_list.remove(tb_name)
        save_default_settings('default_settings.json', setting_name,
                              'testbenches', tb_list)
        save_filter(default_data[setting_name]['json_file'], 'result_filter',
                    'tbc', tb_name, 0)
    else:
        print('No valid input given.')


def browse_file(input_field, default_setting, file_type):
    """This function will be executed if the 'Browse' of the
       'Load filter file' entry was pressed. It will open a window
       from which the file can be chosen.
    """
    file_path = filedialog.askopenfilename()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, file_path)
    save_default_settings('default_settings.json',
                          default_setting, file_type, file_path)


def browse_folder(input_field, default_setting, folder_type):
    """This finction will be executed if the 'Browse' of the
       'Save report excel in' entry was pressed. It will open a window
       from which the folder can be chosen.
    """
    destination_folder = filedialog.askdirectory()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, destination_folder)
    save_default_settings('default_settings.json',
                          default_setting, folder_type,
                          destination_folder)


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
    df_list = write_results_in_template(template_file, res,
                                        filter_data['data_filter'],
                                        row_headers=int(row_number_headers.get()))
    report_excel_folder = loc_report_excel.get()
    report_excel_name = report_file_name.get()
    dataframe_to_excel(df_list, report_excel_folder, report_excel_name)
