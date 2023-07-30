import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter import filedialog
from evaluate_excel import read_filter_json


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
    # Label for entry name
    name_label = tk.Label(new_entry_frame, text='Name of new entry',
                          font=('Arial', 8, 'bold'))
    name_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    # Input line for entry name
    entry_name_input = tk.Entry(new_entry_frame, width=130)
    entry_name_input.grid(row=1, column=0, columnspan=2, sticky='w', padx=10,
                          pady=(0, 5))
    # Label for testcase
    testcase_label = tk.Label(new_entry_frame, text='Testcase',
                              font=('Arial', 8, 'bold'))
    testcase_label.grid(row=2, column=0, sticky='w', padx=10, pady=5)
    # Input line for testcase
    testcase_input = tk.Entry(new_entry_frame, width=60)
    testcase_input.grid(row=3, column=0, sticky='we', padx=10, pady=(0, 5))
    # Label for variable
    variable_label = tk.Label(new_entry_frame, text='Variable',
                              font=('Arial', 8, 'bold'))
    variable_label.grid(row=2, column=1, sticky='w', padx=10, pady=5)
    # Input line for variable
    variable_input = tk.Entry(new_entry_frame, width=60)
    variable_input.grid(row=3, column=1, sticky='we', padx=10, pady=(0, 5))
    # Label for values to be calculated
    variable_label = tk.Label(new_entry_frame, text='Value to calculate',
                              font=('Arial', 8, 'bold'))
    variable_label.grid(row=4, column=0, sticky='w', padx=10, pady=5)
    # Input line for values to be calculated
    variable_input = tk.Entry(new_entry_frame, width=60)
    variable_input.grid(row=5, column=0, sticky='we', padx=10, pady=(0, 5))
    # Label for header in template
    variable_label = tk.Label(new_entry_frame, text='Header in template',
                              font=('Arial', 8, 'bold'))
    variable_label.grid(row=4, column=1, sticky='w', padx=10, pady=5)
    # Input line for header in template
    variable_input = tk.Entry(new_entry_frame, width=60)
    variable_input.grid(row=5, column=1, sticky='we', padx=10, pady=(0, 5))

    # Frame for options
    options_frame = tk.LabelFrame(page, text='Options', bd=2,
                                  relief='ridge')
    options_frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=5)
    # Button for adding new testcase/variable pair
    btn_add_tc = tk.Button(options_frame, text='Add testcase', width=20,
                           command=lambda:
                           add_testcase_variable(window))
    btn_add_tc.grid(row=0, column=0, sticky='nswe', padx=5, pady=5)
    # Button for deleting the last added testcase variable pair
    btn_del_tc = tk.Button(options_frame, text='Delete testcase', width=20,
                           command=lambda:
                           del_testcase_variable(window))
    btn_del_tc.grid(row=0, column=1, sticky='nswe', padx=5, pady=5)
    # Button for adding a new value to calculate and header in template
    btn_add_cal_val = tk.Button(options_frame, text='Add value to calculate',
                                width=20, command=lambda:
                                add_value_to_calculate(window))
    btn_add_cal_val.grid(row=0, column=2, sticky='nswe', padx=5, pady=5)
    # Button for deleting the last added value to calculate
    btn_del_cal_val = tk.Button(options_frame,
                                text='Delete value to calculate',
                                width=20, command=lambda:
                                del_value_to_calculate(window))
    btn_del_cal_val.grid(row=0, column=3, sticky='nswe', padx=5, pady=5)
    # Button for saving the new entry
    btn_save = tk.Button(options_frame, text='Save', width=20,
                         command=lambda: save_entry(window))
    btn_save.grid(row=0, column=4, sticky='nswe', padx=5, pady=5)


def add_testcase_variable(window):
    pass


def del_testcase_variable(window):
    pass


def add_value_to_calculate(window):
    pass


def del_value_to_calculate(window):
    pass


def save_entry(window):
    pass
