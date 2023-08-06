import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
from evaluate_excel import read_filter_json
import UiConfigurateFilterAdd
import UiConfigurateFilterEdit
import UiConfigurateFilterNewFilter


def initialize_page_configurate_filter(window):
    # Create a frame for the page
    page = tk.Frame(window)
    page.grid(row=0, column=0, sticky='nsew')

    # Frame for title
    title_frame = tk.Frame(page, bd=1, relief='raised')
    title_frame.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=10,
                     pady=5)
    # Label for title of creating a filter
    filter_label = tk.Label(title_frame, text='Configurate filter',
                            font=('Arial', 12, 'bold'))
    filter_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)

    # Frame for options
    options_frame = tk.LabelFrame(page, text='Options', bd=2, relief='ridge')
    options_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=5)
    # Frame for buttons (Add, Edit, New filter)
    btns_frame = tk.Frame(options_frame, bd=1)
    btns_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=5)
    # Add info button
    btn_add_info = tk.Button(btns_frame, text='Add', width=7,
                             command=lambda:
                             open_add_page(window, json_file_input.get()))
    btn_add_info.grid(row=0, column=0, sticky='nswe', padx=5, pady=5)
    # Edit button
    btn_edit_info = tk.Button(btns_frame, text='Edit', width=7,
                              command=lambda:
                              open_edit_page(window))
    btn_edit_info.grid(row=1, column=0, sticky='nswe', padx=5, pady=5)
    # Create new filter button
    btn_new_filter = tk.Button(btns_frame, text='New filter', width=7,
                               command=lambda:
                               open_new_filter_page(window))
    btn_new_filter.grid(row=2, column=0, sticky='nswe', padx=5, pady=5)
    # Frame for input line of the filter json file
    filter_input_frame = tk.Frame(options_frame, bd=1)
    filter_input_frame.grid(row=0, column=1, columnspan=2, sticky='nsew',
                            padx=10, pady=5)
    # Label for filter json file path
    json_file_label = tk.Label(filter_input_frame, text='Load filter file:',
                               font=('Arial', 8, 'bold'))
    json_file_label.grid(row=0, column=1, sticky='w')
    # Input line for json file path
    json_file_input = tk.Entry(filter_input_frame, width=130)
    json_file_input.grid(row=1, column=1, sticky='e', padx=5, pady=5)
    btn_browse_filter = tk.Button(filter_input_frame, text='Browse', width=7,
                                  command=lambda:
                                  browse_and_set_infos(json_file_input))
    btn_browse_filter.grid(row=1, column=2, sticky='e', padx=(0, 5), pady=5)

    # Frame for the filter data
    global filter_data_frame
    filter_data_frame = tk.LabelFrame(page, text='Filter data', bd=2,
                                      relief='ridge')
    filter_data_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=5)


def open_add_page(window, filter_file):
    if filter_file != '':
        UiConfigurateFilterAdd.initialize_page_add(window, filter_file)
    else:
        print('No filter file was selected.')


def open_edit_page(window):
    UiConfigurateFilterEdit.initialize_page_edit(window)


def open_new_filter_page(window):
    UiConfigurateFilterNewFilter.initialize_page_new_filter(window)


def browse_and_set_infos(input_field):
    # Load data_filter from json file
    json_file = browse_file(input_field)
    global data_filter
    data_filter = read_filter_json(json_file)['data_filter']
    # Frame for list box
    listbox_frame = tk.Frame(filter_data_frame, bd=1, relief='ridge')
    listbox_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=5)
    # Listbox for informations of the filter
    info_listbox = tk.Listbox(listbox_frame, height=13)
    info_listbox.grid(row=0, column=0, sticky='nsew', padx=10, pady=5)
    info_listbox.bind('<<ListboxSelect>>', display_filter_data)
    # Add scrollbar to the listbox
    scrollbar = tk.Scrollbar(listbox_frame, orient='vertical')
    scrollbar.grid(row=0, column=1, sticky='nse')
    info_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=info_listbox.yview)
    # List of all informations
    info_list = list(data_filter)
    for item in info_list:
        info_listbox.insert('end', item)


def browse_file(input_field):
    """This function will be executed if the 'Browse' of the
       'Load filter file' entry was pressed. It will open a window
       from which the file can be chosen.
    """
    file_path = filedialog.askopenfilename()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, file_path)
    return file_path


def display_filter_data(event_object):
    # If a lisbox item is selected an event object is delivered to
    # display_filter_infos
    # Get filter data of the selected listbox item
    selected_item = listbox_item_select(event_object)
    tc_var_dict = data_filter[selected_item][1]
    tc_var_df = pd.DataFrame(tc_var_dict.items(), columns=['Testcases',
                                                           'Variables'])
    valcalc_dict = data_filter[selected_item][2]
    val_cal_df = pd.DataFrame(valcalc_dict.items(),
                              columns=['Calculate value',
                                       'Template header'])
    # Display filter data of the selected item
    load_tc_and_var(tc_var_df)
    load_values_to_calculate(val_cal_df)


def listbox_item_select(event_object):
    evob = event_object.widget
    index = int(evob.curselection()[0])
    value = evob.get(index)
    return value


def load_tc_and_var(df_tc_var):
    # Frame for testcases and variables
    tc_var_frame = tk.Frame(filter_data_frame, bd=1)
    tc_var_frame.grid(row=2, column=1, sticky='nsew', padx=10, pady=5)
    # Create a treeview widget
    tree = ttk.Treeview(tc_var_frame, show='headings')
    tree.grid(row=0, column=1, sticky='nsew')
    # Set up columns
    tree['columns'] = list(df_tc_var.columns)
    for column in df_tc_var.columns:
        tree.column(column, anchor="center", width=200, stretch=tk.NO)
        tree.heading(column, text=column)
    # Insert data from dataframe into the
    for _, row in df_tc_var.iterrows():
        tree.insert('', 'end', values=list(row))
    # Add a vertical scrollbar
    scrollbar_tc_var = tk.Scrollbar(tc_var_frame, orient='vertical')
    scrollbar_tc_var.grid(row=0, column=1, sticky='nse')
    tree.config(yscrollcommand=scrollbar_tc_var.set)
    scrollbar_tc_var.config(command=tree.yview)


def load_values_to_calculate(valcalc_dict):
    # Frame for values to calculate
    valcalc_frame = tk.Frame(filter_data_frame, bd=1)
    valcalc_frame.grid(row=2, column=2, sticky='nsew', padx=10, pady=5)
    # Create a treeview widget
    tree = ttk.Treeview(valcalc_frame, show='headings')
    tree.grid(row=0, column=0, sticky='nsew')
    # Set up columns
    tree['columns'] = list(valcalc_dict.columns)
    for column in valcalc_dict.columns:
        tree.column(column, anchor="center", width=130, stretch=tk.NO)
        tree.heading(column, text=column)
    # Insert data from dataframe into the
    for _, row in valcalc_dict.iterrows():
        tree.insert('', 'end', values=list(row))
    # Add a vertical scrollbar
    scrollbar_valcalc = tk.Scrollbar(valcalc_frame, orient='vertical')
    scrollbar_valcalc.grid(row=0, column=1, sticky='nse')
    tree.config(yscrollcommand=scrollbar_valcalc.set)
    scrollbar_valcalc.config(command=tree.yview)
