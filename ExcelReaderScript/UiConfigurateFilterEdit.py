import tkinter as tk
from evaluate_excel import read_filter_json
from UiConfigurateFilterAdd import InputLineCreator


def initialize_page_edit(window, filter_file, sel_entry):
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
    ######################################################################
    # Frame for edit filter data
    edit_entry_frame = tk.LabelFrame(page, text='Edit filter data', bd=2,
                                     relief='ridge')
    edit_entry_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=5)

    # Frame for edit entry name
    edit_name_frame = tk.Frame(edit_entry_frame, relief='ridge')
    edit_name_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=5)
    # Label for edit entry name
    name_label = tk.Label(edit_name_frame, text='Edit name of entry',
                          font=('Arial', 8, 'bold'))
    name_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    # Input line for entry name
    edit_name_input = tk.Entry(edit_name_frame, width=124)
    edit_name_input.grid(row=1, column=0, columnspan=2, sticky='w', padx=10,
                         pady=(0, 5))
    edit_name_input.insert(0, sel_entry)

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
    options_frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=5)
    # Button for deleting the complete entry
    btn_del_entry = tk.Button(options_frame, text='Delete complete entry',
                              width=20, command=lambda:
                              del_complete_entry())
    btn_del_entry.grid(row=0, column=0, sticky='nswe', padx=5, pady=5)
    # Button for adding testcase and variable pair
    btn_add_testcase = tk.Button(options_frame, text='Add testcase', width=20,
                                 command=lambda:
                                 add_entry_line())
    btn_add_testcase.grid(row=0, column=1, sticky='nswe', padx=5, pady=5)
    # Button for deleting testcase and variable
    btn_del_testcase = tk.Button(options_frame, text='Delete testcase',
                                 width=20, command=lambda:
                                 del_entry_line())
    btn_del_testcase.grid(row=0, column=2, sticky='nswe', padx=5, pady=5)
    # Button for adding value to calculate and header in template
    btn_add_valcalc = tk.Button(options_frame, text='Add value to calculate',
                                width=20, command=lambda:
                                add_entry_line())
    btn_add_valcalc.grid(row=0, column=3, sticky='nswe', padx=5, pady=5)
    # Button for deleting value to calculate and header in template
    btn_del_valcalc = tk.Button(options_frame,
                                text='Delete value to calculate',
                                width=20, command=lambda:
                                del_entry_line())
    btn_del_valcalc.grid(row=0, column=4, sticky='nswe', padx=5, pady=5)
    # Button for saving the changes
    btn_save_changes = tk.Button(options_frame, text='Save changes', width=20,
                                 command=lambda:
                                 save_changes())
    btn_save_changes.grid(row=1, column=2, sticky='nswe', padx=5, pady=5)


def del_complete_entry():
    pass


def add_entry_line():
    pass


def del_entry_line():
    pass


def save_changes():
    pass
