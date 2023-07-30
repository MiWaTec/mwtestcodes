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
    selected_filter_label.grid(row=1, column=0, sticky='w', padx=10, pady=5)

    # Frame for adding data
    new_entry_frame = tk.LabelFrame(page, text='Data', bd=2, relief='ridge')
    new_entry_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=5)
