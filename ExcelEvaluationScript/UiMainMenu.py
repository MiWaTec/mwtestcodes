import tkinter as tk
import json
import UiMainMenuCreateNewSetting
from UiElementCreator import ButtonCreator
from evaluate_excel import read_filter_json

available_set_frame = None


def initialize_page_main_menu(window):
    # Page main menu
    page1 = tk.Frame(window)
    page1.grid(row=0, column=0, sticky='nsew')

    # Frame for available settings
    global available_set_frame
    available_set_frame = tk.LabelFrame(page1, text='Available settings',
                                        bd=2, relief='ridge')
    available_set_frame.grid(row=1, column=1, sticky='nsew', padx=10,
                             pady=5)

    # Label for options
    options_frame = tk.LabelFrame(page1, text='Options', bd=2,
                                  relief='ridge', height=150, width=200)
    options_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=5)

    # Button for creating a new setting
    btn_new_setting = tk.Button(options_frame, text='Create new setting',
                                width=16, height=1, command=lambda:
                                create_setting(window))
    btn_new_setting.grid(column=0, row=1, sticky='we', padx=10, pady=5)
    # Button for removing an existing setting
    btn_create_new_setting = tk.Button(options_frame, text='Remove setting',
                                       width=16, height=1, command=lambda:
                                       remove_setting(input_del_setting.get(),
                                                      window))
    btn_create_new_setting.grid(column=0, row=2, sticky='we', padx=10, pady=5)
    input_del_setting = tk.Entry(options_frame, width=16)
    input_del_setting.grid(column=0, row=3, sticky='we', padx=10, pady=5)


def create_setting(window):
    UiMainMenuCreateNewSetting.initialize_page_create_setting(window)


def remove_setting(setting: str, window):
    """This function deletes the given setting from the default_settings.json
       and from the UI main page.

    Args:
        setting (str): Name of the setting that will be removed.
    """
    settings_dict = read_filter_json('default_settings.json')
    del settings_dict[setting]
    with open('default_settings.json', 'w') as f:
        json.dump(settings_dict, f, indent=4)
    unload_available_settings()
    load_available_settings('default_settings.json', window)


def load_available_settings(default_json_file, window):
    settings_dict = read_filter_json(default_json_file)
    for setting in settings_dict:
        ButtonCreator(setting, available_set_frame, window)


def unload_available_settings():
    btn_list = ButtonCreator.get_all_instances()
    for btn in btn_list:
        ButtonCreator.delete_button(btn)
    ButtonCreator._counter = 1
