import tkinter as tk
import json
from evaluate_excel import read_filter_json
import UiConfigurateFilter
from UiConfigurateFilterAdd import InputLineCreator


def initialize_page_edit(window, filter_file, sel_entry):
    # Clean up input line objects of the InputLineCreator class
    InputLineCreator.clean_up_objects()
    # Load selected data from filter file
    sel_data = read_filter_json(filter_file)['data_filter'][sel_entry]
    # Create a frame for the page
    page = tk.Frame(window)
    page.grid(row=0, column=0, sticky='nsew')

    # Frame for title
    title_frame = tk.Frame(page, bd=1, relief='raised')
    title_frame.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=10,
                     pady=5)
    # Label for title of creating a filter
    filter_label = tk.Label(title_frame, text='Edit entry of the filter',
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

    # Frame for name of the selected entry
    selected_entry_frame = tk.LabelFrame(page, text='Selected entry', bd=2,
                                         relief='ridge')
    selected_entry_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=5)
    # Label for name of the selected entry
    edit_name_input = tk.Label(selected_entry_frame, text=sel_entry,
                               font=('Arial', 8, 'bold'))
    edit_name_input.grid(row=1, column=0, columnspan=2, sticky='w', padx=10,
                         pady=(0, 5))

    # Frame for edit filter data
    edit_entry_frame = tk.LabelFrame(page, text='Edit filter data', bd=2,
                                     relief='ridge')
    edit_entry_frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=5)
    # Frame for edit testcase and variable
    edit_testcase_frame = tk.Frame(edit_entry_frame, relief='ridge')
    edit_testcase_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=5)
    # Label for edit testcase
    edit_testcase_label = tk.Label(edit_testcase_frame, text='Edit testcase',
                                   font=('Arial', 8, 'bold'))
    edit_testcase_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    # Label for edit variable
    edit_variable_label = tk.Label(edit_testcase_frame,
                                   text='Edit variable of testcase',
                                   font=('Arial', 8, 'bold'))
    edit_variable_label.grid(row=0, column=1, sticky='w', padx=10, pady=5)
    # Input lines for edit testcase and variable
    for key, value in sel_data[1].items():
        InputLineCreator(edit_testcase_frame, 'testcases')
        last_entry = InputLineCreator.get_all_instances('testcases')[-1]
        InputLineCreator.insert_text_entry_obj(last_entry[0], 'col1', key)
        InputLineCreator.insert_text_entry_obj(last_entry[1], 'col2', value)

    # Frame for edit value to calculate entry and header in template entry
    edit_calcvalue_frame = tk.Frame(edit_entry_frame, relief='ridge')
    edit_calcvalue_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=5)
    # Label for edit values to be calculated
    edit_variable_label = tk.Label(edit_calcvalue_frame,
                                   text='Edit value to calculate',
                                   font=('Arial', 8, 'bold'))
    edit_variable_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    # Label for edit header in template
    edit_header_label = tk.Label(edit_calcvalue_frame,
                                 text='Edit header in the template',
                                 font=('Arial', 8, 'bold'))
    edit_header_label.grid(row=0, column=1, sticky='w', padx=10, pady=5)
    # Input line for edit values to be calculated and header in template
    for key, value in sel_data[2].items():
        InputLineCreator(edit_calcvalue_frame, 'calc_value')
        last_entry = InputLineCreator.get_all_instances('calc_value')[-1]
        InputLineCreator.insert_text_entry_obj(last_entry[0], 'col1', key)
        InputLineCreator.insert_text_entry_obj(last_entry[1], 'col2', value)

    # Frame for options
    options_frame = tk.LabelFrame(page, text='Options', bd=2,
                                  relief='ridge')
    options_frame.grid(row=4, column=0, sticky='nsew', padx=10, pady=5)
    # Button for deleting the complete entry
    btn_del_entry = tk.Button(options_frame, text='Delete complete entry',
                              width=20, command=lambda:
                              del_complete_entry(filter_file, sel_entry,
                                                 window))
    btn_del_entry.grid(row=0, column=0, sticky='nswe', padx=5, pady=5)
    # Button for adding testcase and variable pair
    btn_add_testcase = tk.Button(options_frame, text='Add testcase', width=20,
                                 command=lambda:
                                 add_entry_line(edit_testcase_frame,
                                                'testcases'))
    btn_add_testcase.grid(row=0, column=1, sticky='nswe', padx=5, pady=5)
    # Button for deleting testcase and variable
    btn_del_testcase = tk.Button(options_frame, text='Delete testcase',
                                 width=20, command=lambda:
                                 del_last_entry_line('testcases'))
    btn_del_testcase.grid(row=0, column=2, sticky='nswe', padx=5, pady=5)
    # Button for adding value to calculate and header in template
    btn_add_valcalc = tk.Button(options_frame, text='Add value to calculate',
                                width=20, command=lambda:
                                add_entry_line(edit_calcvalue_frame,
                                               'calc_value'))
    btn_add_valcalc.grid(row=0, column=3, sticky='nswe', padx=5, pady=5)
    # Button for deleting value to calculate and header in template
    btn_del_valcalc = tk.Button(options_frame,
                                text='Delete value to calculate',
                                width=20, command=lambda:
                                del_last_entry_line('calc_value'))
    btn_del_valcalc.grid(row=0, column=4, sticky='nswe', padx=5, pady=5)
    # Button for saving the changes
    btn_save_changes = tk.Button(options_frame, text='Save changes', width=20,
                                 command=lambda:
                                 save_changes(filter_file, sel_entry, window))
    btn_save_changes.grid(row=1, column=2, sticky='nswe', padx=5, pady=5)


def del_complete_entry(filter_file, entry_name_input, window):
    # Load the filter data from json file
    filter_data = read_filter_json(filter_file)
    # Delete the complete entry from the filter file
    del filter_data['data_filter'][entry_name_input]
    # Save changes to the filter file
    with open(filter_file, 'w') as f:
        json.dump(filter_data, f, indent=4)
    # Switch to configurate filter first page
    UiConfigurateFilter.initialize_page_configurate_filter(window, filter_file)
    UiConfigurateFilter.set_infos(filter_file)


def add_entry_line(frame, input_type):
    InputLineCreator(frame, input_type)


def del_last_entry_line(input_type):
    all_instances = InputLineCreator.get_all_instances(input_type)
    if len(all_instances) < 2:
        return None
    last_entry_line = InputLineCreator.get_all_instances(input_type)[-1]
    InputLineCreator.delete_entry_line(last_entry_line[0], 'col1')
    InputLineCreator.delete_obj_instances_dict(input_type, 'col1',
                                               last_entry_line[0])
    InputLineCreator.delete_entry_line(last_entry_line[1], 'col2')
    InputLineCreator.delete_obj_instances_dict(input_type, 'col2',
                                               last_entry_line[1])
    InputLineCreator.instances_dict[input_type]['row'] -= 1


def save_changes(filter_file, entry_name_input, window):
    # Get the texts of all testcase/variable inputs
    tc_var_dict = {}
    tc_var = InputLineCreator.get_all_instances('testcases')
    for instance in tc_var:
        testcase = InputLineCreator.get_text(instance[0], 'col1')
        variable = InputLineCreator.get_text(instance[1], 'col2')
        tc_var_dict[testcase] = variable
    # Get the texts of all value to calculate/template header inputs
    valcalc_tempheader_dict = {}
    valcalc_tempheader = InputLineCreator.get_all_instances('calc_value')
    for instance in valcalc_tempheader:
        valcalc = InputLineCreator.get_text(instance[0], 'col1')
        tempheader = InputLineCreator.get_text(instance[1], 'col2')
        valcalc_tempheader_dict[valcalc] = tempheader
    # Load the filter data from json file
    filter_data = read_filter_json(filter_file)
    # Add the new entry to the dict of the filter file
    filter_data['data_filter'][entry_name_input] = \
        [list(valcalc_tempheader_dict),
         tc_var_dict, valcalc_tempheader_dict]
    # Save changes to the filter file
    with open(filter_file, 'w') as f:
        json.dump(filter_data, f, indent=4)
    # Switch to configurate filter first page
    UiConfigurateFilter.initialize_page_configurate_filter(window, filter_file)
    UiConfigurateFilter.set_infos(filter_file)
