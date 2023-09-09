import tkinter as tk
import json
import UiConfigurateFilter
import UiElementCreator
from evaluate_excel import read_filter_json


def initialize_page_add(window, filter_file):
    # Clean up input line objects of the InputLineCreator class
    UiElementCreator.InputLineCreator.clean_up_objects()
    # Create a frame for the page
    page = tk.Frame(window)
    page.grid(row=0, column=0, sticky='nsew')

    # Frame for title
    title_frame = tk.Frame(page, bd=1, relief='raised')
    title_frame.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=10,
                     pady=5)
    # Label for title of creating a filter
    filter_label = tk.Label(title_frame, text='Add new entry to filter',
                            font=('Arial', 12, 'bold'))
    filter_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)

    # Frame for selected filter json
    selected_filter_frame = tk.LabelFrame(page, text='Selected filter file',
                                          bd=2, relief='ridge')
    selected_filter_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=5)
    # Label for the name of the selected filter json
    selected_filter_label = tk.Label(selected_filter_frame, text=filter_file,
                                     font=('Arial', 8, 'bold'))
    selected_filter_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)

    # Frame for new filter data
    new_entry_frame = tk.LabelFrame(page, text='New filter data', bd=2,
                                    relief='ridge')
    new_entry_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=5)

    # Frame for entry name
    entry_name_frame = tk.Frame(new_entry_frame, relief='ridge')
    entry_name_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=5)
    # Label for entry name
    name_label = tk.Label(entry_name_frame, text='Name of new entry',
                          font=('Arial', 8, 'bold'))
    name_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    # Input line for entry name
    entry_name_input = tk.Entry(entry_name_frame, width=124)
    entry_name_input.grid(row=1, column=0, columnspan=2, sticky='w', padx=10,
                          pady=(0, 5))

    # Frame for testcase entry and variable entry
    new_testcase_frame = tk.Frame(new_entry_frame, relief='ridge')
    new_testcase_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=5)
    # Label for testcase
    testcase_label = tk.Label(new_testcase_frame, text='Testcase',
                              font=('Arial', 8, 'bold'))
    testcase_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    # Label for variable
    variable_label = tk.Label(new_testcase_frame,
                              text='Variable of the testcase',
                              font=('Arial', 8, 'bold'))
    variable_label.grid(row=0, column=1, sticky='w', padx=10, pady=5)
    # Input lines for testcase and variable
    UiElementCreator.InputLineCreator(new_testcase_frame, 'testcases')

    # Frame for value to calculate entry and header in template entry
    new_calcvalue_frame = tk.Frame(new_entry_frame, relief='ridge')
    new_calcvalue_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=5)
    # Label for values to be calculated
    variable_label = tk.Label(new_calcvalue_frame, text='Value to calculate',
                              font=('Arial', 8, 'bold'))
    variable_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    # Label for header in template
    header_label = tk.Label(new_calcvalue_frame,
                            text='Header in the template',
                            font=('Arial', 8, 'bold'))
    header_label.grid(row=0, column=1, sticky='w', padx=10, pady=5)
    # Input line for values to be calculated and header in template
    UiElementCreator.InputLineCreator(new_calcvalue_frame, 'calc_value')

    # Frame for options
    options_frame = tk.LabelFrame(page, text='Options', bd=2,
                                  relief='ridge')
    options_frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=5)
    # Button for adding new testcase/variable pair
    btn_add_tc = tk.Button(options_frame, text='Add testcase', width=20,
                           command=lambda:
                           add_entry_line(new_testcase_frame, 'testcases'))
    btn_add_tc.grid(row=0, column=0, sticky='nswe', padx=5, pady=5)
    # Button for deleting the last added testcase variable pair
    btn_del_tc = tk.Button(options_frame, text='Delete testcase', width=20,
                           command=lambda:
                           del_last_entry_line('testcases'))
    btn_del_tc.grid(row=0, column=1, sticky='nswe', padx=5, pady=5)
    # Button for adding a new value to calculate and header in template
    btn_add_cal_val = tk.Button(options_frame, text='Add value to calculate',
                                width=20, command=lambda:
                                add_entry_line(new_calcvalue_frame,
                                               'calc_value'))
    btn_add_cal_val.grid(row=0, column=2, sticky='nswe', padx=5, pady=5)
    # Button for deleting the last added value to calculate
    btn_del_cal_val = tk.Button(options_frame,
                                text='Delete value to calculate',
                                width=20, command=lambda:
                                del_last_entry_line('calc_value'))
    btn_del_cal_val.grid(row=0, column=3, sticky='nswe', padx=5, pady=5)
    # Button for saving the new entry
    btn_save = tk.Button(options_frame, text='Save', width=20,
                         command=lambda: save_entry(filter_file,
                                                    entry_name_input.get(),
                                                    window))
    btn_save.grid(row=0, column=4, sticky='nswe', padx=5, pady=5)


def add_entry_line(frame, input_type):
    UiElementCreator.InputLineCreator(frame, input_type)


def del_last_entry_line(input_type):
    all_instances = UiElementCreator.InputLineCreator.get_all_instances(input_type)
    if len(all_instances) < 2:
        return None
    last_entry_line = UiElementCreator.InputLineCreator.get_all_instances(input_type)[-1]
    UiElementCreator.InputLineCreator.delete_entry_line(last_entry_line[0], 'col1')
    UiElementCreator.InputLineCreator.delete_obj_instances_dict(input_type, 'col1',
                                                                last_entry_line[0])
    UiElementCreator.InputLineCreator.delete_entry_line(last_entry_line[1], 'col2')
    UiElementCreator.InputLineCreator.delete_obj_instances_dict(input_type, 'col2',
                                                                last_entry_line[1])
    UiElementCreator.InputLineCreator.instances_dict[input_type]['row'] -= 1


def save_entry(filter_file, entry_name_input, window):
    # Get the texts of all testcase/variable inputs
    tc_var_dict = {}
    tc_var = UiElementCreator.InputLineCreator.get_all_instances('testcases')
    for instance in tc_var:
        testcase = UiElementCreator.InputLineCreator.get_text(instance[0], 'col1')
        variable = UiElementCreator.InputLineCreator.get_text(instance[1], 'col2')
        tc_var_dict[testcase] = variable
    # Get the texts of all value to calculate/template header inputs
    valcalc_tempheader_dict = {}
    valcalc_tempheader = UiElementCreator.InputLineCreator.get_all_instances('calc_value')
    for instance in valcalc_tempheader:
        valcalc = UiElementCreator.InputLineCreator.get_text(instance[0], 'col1')
        tempheader = UiElementCreator.InputLineCreator.get_text(instance[1], 'col2')
        valcalc_tempheader_dict[valcalc] = tempheader
    # Load the filter data from json file
    filter_data = read_filter_json(filter_file)
    # Add the new entry to the dict of the filter file
    filter_data['data_filter'][entry_name_input] = \
        [list(valcalc_tempheader_dict),
         tc_var_dict, valcalc_tempheader_dict]
    # Save new entry to the filter file
    with open(filter_file, 'w') as f:
        json.dump(filter_data, f, indent=4)
    # Switch to back to the configurate filter page
    UiConfigurateFilter.initialize_page_configurate_filter(window, filter_file)
    UiConfigurateFilter.set_infos(filter_file)
