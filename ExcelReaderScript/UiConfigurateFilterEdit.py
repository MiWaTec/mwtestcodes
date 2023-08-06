import tkinter as tk
from evaluate_excel import read_filter_json


def initialize_page_edit(window, filter_file, sel_entry):
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

    # Frame for edit selected entry
    edit_entry_frame = tk.LabelFrame(page, text='Edit selected entry', bd=2,
                                     relief='ridge')
    edit_entry_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=5)
    # Label for entry name
    name_label = tk.Label(edit_entry_frame, text='Edit name',
                          font=('Arial', 8, 'bold'))
    name_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    # Input line for edit name
    edit_name_input = tk.Entry(edit_entry_frame, width=124)
    edit_name_input.grid(row=1, column=0, columnspan=2, sticky='w', padx=10,
                         pady=(0, 5))
    # Label for edit testcase
    edit_testcase_label = tk.Label(edit_entry_frame, text='Edit testcase',
                                   font=('Arial', 8, 'bold'))
    edit_testcase_label.grid(row=2, column=0, sticky='w', padx=10, pady=5)
    # Input line for edit testcase
    edit_testcase_input = tk.Entry(edit_entry_frame, width=60)
    edit_testcase_input.grid(row=3, column=0, sticky='w', padx=10, pady=(0, 5))
    # Label for edit variable
    edit_variable_label = tk.Label(edit_entry_frame,
                                   text='Edit variable of the testcase',
                                   font=('Arial', 8, 'bold'))
    edit_variable_label.grid(row=2, column=1, sticky='w', padx=10, pady=5)
    # Input line for edit variable
    edit_variable_input = tk.Entry(edit_entry_frame, width=60)
    edit_variable_input.grid(row=3, column=1, sticky='w', padx=10, pady=(0, 5))

    # Label for edit value to calculate
    edit_valcalc_label = tk.Label(edit_entry_frame,
                                  text='Edit value to calculate',
                                  font=('Arial', 8, 'bold'))
    edit_valcalc_label.grid(row=4, column=0, sticky='w', padx=10, pady=5)
    # Input line for edit testcase
    edit_valcalc_input = tk.Entry(edit_entry_frame, width=60)
    edit_valcalc_input.grid(row=5, column=0, sticky='w', padx=10, pady=(0, 5))
    # Label for edit header in template
    edit_header_label = tk.Label(edit_entry_frame,
                                 text='Edit header in template',
                                 font=('Arial', 8, 'bold'))
    edit_header_label.grid(row=4, column=1, sticky='w', padx=10, pady=5)
    # Input line for edit header in template
    edit_testcase_input = tk.Entry(edit_entry_frame, width=60)
    edit_testcase_input.grid(row=5, column=1, sticky='w', padx=10,
                             pady=(0, 5))

    # Frame for options
    options_frame = tk.LabelFrame(page, text='Options', bd=2,
                                  relief='ridge')
    options_frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=5)
    # Button for deleting the complete entry
    btn_del_entry = tk.Button(options_frame, text='Delete complete entry',
                              width=52, command=lambda:
                              del_complete_entry())
    btn_del_entry.grid(row=0, column=0, sticky='nswe', padx=5, pady=5)
    # Button for saving the changes
    btn_save_changes = tk.Button(options_frame, text='Save changes', width=52,
                                 command=lambda:
                                 save_changes())
    btn_save_changes.grid(row=0, column=1, sticky='nswe', padx=5, pady=5)

    # Set filter data of the selected item
    sel_data = read_filter_json(filter_file)['data_filter'][sel_entry]
    print(sel_data)
    edit_name_input.insert(0, sel_entry)


def del_complete_entry():
    pass


def add_entry_line():
    pass


def del_entry_line():
    pass


def save_changes():
    pass
