import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter import filedialog
from evaluate_excel import read_filter_json


class InputLineCreator:
    instances_dict = {
        'testcases': {
            'testcases': [],
            'tc_variables': [],
            'row': 2
        },
        'calc_value': {
            'value_to_calc': [],
            'header_template': [],
            'row': 2
        }
    }

    def __init__(self, frame, input_type) -> None:
        self.input_line_col1 = tk.Entry(frame, width=60)
        self.input_line_col1.grid(column=0,
                                  row=InputLineCreator.instances_dict[input_type]['row'],
                                  sticky='we', padx=10, pady=(0, 5))
        self.input_line_col2 = tk.Entry(frame, width=60)
        self.input_line_col2.grid(column=1,
                                  row=InputLineCreator.instances_dict[input_type]['row'],
                                  sticky='we', padx=10, pady=(0, 5))
        if input_type == 'testcases':
            InputLineCreator.instances_dict[input_type]['testcases'].append(self.input_line_col1)
            InputLineCreator.instances_dict[input_type]['tc_variables'].append(self.input_line_col2)
            InputLineCreator.instances_dict[input_type]['row'] += 1
        elif input_type == 'calc_value':
            InputLineCreator.instances_dict[input_type]['value_to_calc'].append(self.input_line_col1)
            InputLineCreator.instances_dict[input_type]['header_template'].append(self.input_line_col2)
            InputLineCreator.instances_dict[input_type]['row'] += 1

    def get_all_instances(input_type) -> list:
        """This function returns a list of all created instances of the class.

        Returns:
            list: A list of all instances of the class that were instantiated.
        """
        if input_type == 'testcases':
            return InputLineCreator.calc_value_dict['instances']
        elif input_type == 'calc_value':
            return InputLineCreator.calc_value_dict['instances']

    def delete_button(self: object):
        """This function deletes the given class object.

        Args:
            self (object): Instance of the class that will be deleted.
        """
        self.input_line.destroy()


def initialize_page_add(window, filter_file):
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
    entry_name_input = tk.Entry(entry_name_frame, width=130)
    entry_name_input.grid(row=1, column=0, columnspan=2, sticky='w', padx=10,
                          pady=(0, 5))

    # Frame for testcase entry and variable entry
    new_testcase_frame = tk.Frame(new_entry_frame, relief='ridge')
    new_testcase_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=5)
    # Label for testcase
    testcase_label = tk.Label(new_testcase_frame, text='Testcase',
                              font=('Arial', 8, 'bold'))
    testcase_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    # Input line for testcase
    testcase_input = tk.Entry(new_testcase_frame, width=60)
    testcase_input.grid(row=1, column=0, sticky='we', padx=10, pady=(0, 5))
    # Label for variable
    variable_label = tk.Label(new_testcase_frame,
                              text='Variable of the testcase',
                              font=('Arial', 8, 'bold'))
    variable_label.grid(row=0, column=1, sticky='w', padx=10, pady=5)
    # Input line for variable
    variable_input = tk.Entry(new_testcase_frame, width=60)
    variable_input.grid(row=1, column=1, sticky='we', padx=10, pady=(0, 5))

    # Frame for value to calculate entry and header in template entry
    new_calcvalue_frame = tk.Frame(new_entry_frame, relief='ridge')
    new_calcvalue_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=5)
    # Label for values to be calculated
    variable_label = tk.Label(new_calcvalue_frame, text='Value to calculate',
                              font=('Arial', 8, 'bold'))
    variable_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    # Input line for values to be calculated
    variable_input = tk.Entry(new_calcvalue_frame, width=60)
    variable_input.grid(row=1, column=0, sticky='we', padx=10, pady=(0, 5))
    # Label for header in template
    variable_label = tk.Label(new_calcvalue_frame,
                              text='Header in the template',
                              font=('Arial', 8, 'bold'))
    variable_label.grid(row=0, column=1, sticky='w', padx=10, pady=5)
    # Input line for header in template
    variable_input = tk.Entry(new_calcvalue_frame, width=60)
    variable_input.grid(row=1, column=1, sticky='we', padx=10, pady=(0, 5))

    # Frame for options
    options_frame = tk.LabelFrame(page, text='Options', bd=2,
                                  relief='ridge')
    options_frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=5)
    # Button for adding new testcase/variable pair
    btn_add_tc = tk.Button(options_frame, text='Add testcase', width=20,
                           command=lambda:
                           add_testcase_variable(new_testcase_frame,
                                                 'testcases'))
    btn_add_tc.grid(row=0, column=0, sticky='nswe', padx=5, pady=5)
    # Button for deleting the last added testcase variable pair
    btn_del_tc = tk.Button(options_frame, text='Delete testcase', width=20,
                           command=lambda:
                           del_testcase_variable(new_testcase_frame,
                                                 'testcases'))
    btn_del_tc.grid(row=0, column=1, sticky='nswe', padx=5, pady=5)
    # Button for adding a new value to calculate and header in template
    btn_add_cal_val = tk.Button(options_frame, text='Add value to calculate',
                                width=20, command=lambda:
                                add_value_to_calculate(new_calcvalue_frame,
                                                       'calc_value'))
    btn_add_cal_val.grid(row=0, column=2, sticky='nswe', padx=5, pady=5)
    # Button for deleting the last added value to calculate
    btn_del_cal_val = tk.Button(options_frame,
                                text='Delete value to calculate',
                                width=20, command=lambda:
                                del_value_to_calculate(new_calcvalue_frame,
                                                       'calc_value'))
    btn_del_cal_val.grid(row=0, column=3, sticky='nswe', padx=5, pady=5)
    # Button for saving the new entry
    btn_save = tk.Button(options_frame, text='Save', width=20,
                         command=lambda: save_entry(window))
    btn_save.grid(row=0, column=4, sticky='nswe', padx=5, pady=5)


def add_testcase_variable(frame, input_type):
    InputLineCreator(frame, input_type)


def del_testcase_variable(frame, input_type):
    pass


def add_value_to_calculate(frame, input_type):
    InputLineCreator(frame, input_type)


def del_value_to_calculate(frame, input_type):
    pass


def save_entry(frame):
    pass
