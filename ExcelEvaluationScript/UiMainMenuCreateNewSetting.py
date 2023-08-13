import tkinter as tk
import json
import UiSettingMenu
from evaluate_excel import read_filter_json


def initialize_page_create_setting(window):
    # Page create setting
    page2 = tk.Frame(window)
    page2.grid(row=0, column=0, sticky='nsew')
    page2.columnconfigure((0, 1, 2), weight=1)
    page2.rowconfigure((0, 1, 2, 3), weight=1)

    # Label for creating a new setting
    new_setting_label = tk.Label(page2, text='Enter name for the new setting:',
                                 font=('Arial', 14, 'bold'))
    new_setting_label.grid(column=1, row=1, sticky='n')

    # Input line for the name of the new setting
    input_name_new_setting = tk.Entry(page2, width=38)
    input_name_new_setting.grid(column=1, row=2, sticky='n')

    # Button for setting up the new setting
    btn_set_new_setting = tk.Button(page2, text='Create', width=32,
                                    command=lambda:
                                    set_new_setting(input_name_new_setting.get(),
                                                    window))
    btn_set_new_setting.grid(column=1, row=3, sticky='n')


def set_new_setting(setting_name: str, window):
    """This function adds a new setting to the default_settings.json and opens
       the new created setting in the UI.

    Args:
        setting_name (str): _description_
    """
    default_dict = {
        'json_file': '',
        'results_folder': '',
        'template_file': '',
        'row_number_headers': '',
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
    UiSettingMenu.unload_settings()
    UiSettingMenu.initialize_page_setting(window)
    UiSettingMenu.load_settings(setting_name)
