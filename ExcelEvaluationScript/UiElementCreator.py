import tkinter as tk
from tkinter import ttk
import UiSettingMenu
from evaluate_excel import save_filter
import CalcFunctions


class ButtonCreator:
    _instances = []
    _counter = 1

    def __init__(self, name, frame, window) -> None:
        self.name = name
        self.frame = frame
        self.setting_button = tk.Button(self.frame, text=self.name,
                                        width=20, height=2,
                                        command=lambda:
                                        self.setting_button_used(window))
        self.setting_button.grid(column=1, row=ButtonCreator._counter,
                                 padx=5, pady=5)
        ButtonCreator._counter += 1
        ButtonCreator._instances.append(self)

    def setting_button_used(self, window):
        UiSettingMenu.initialize_page_setting(window)
        UiSettingMenu.unload_settings()
        UiSettingMenu.load_settings(self.name)

    def get_all_instances() -> list:
        """This function returns a list of all created instances of the class.

        Returns:
            list: A list of all instances of the class that were instantiated.
        """
        return ButtonCreator._instances

    def delete_button(self: object):
        """This function deletes the given class object.

        Args:
            self (object): Instance of the class that will be deleted.
        """
        self.setting_button.destroy()


class CheckboxCreator:
    _instances = []
    _counter = 0

    def __init__(self, name, frame, filter_file) -> None:
        self.frame = frame
        self.name = name
        self.checked_state = tk.IntVar()
        self.checkbutton = tk.Checkbutton(frame,
                                          text=self.name[:-4],
                                          variable=self.checked_state,
                                          command=lambda:
                                          self.checkbutton_used(filter_file))
        self.checkbutton.grid(column=0, row=CheckboxCreator._counter+4,
                              sticky='nw', columnspan=2, padx=5, pady=5)
        CheckboxCreator._counter += 1
        CheckboxCreator._instances.append(self)

    def checkbutton_used(self, filter_file):
        """This function will be executed after a testbench checkbox of the
           UI was clicked. The state of the checkbox will be saved in the
           filter data json file. If the state is deactivated, the testbench
           will be removed from the filter file. If the state is activated, the
           testbench name will be added in the filter file.
        """
        state = self.checked_state.get()
        save_filter(filter_file, 'result_filter', 'tbc',
                    self.name, state)

    def get_all_instances() -> list:
        """This function returns a list of all created instances of the class.

        Returns:
            list: A list of all instances of the class that were instantiated.
        """
        return CheckboxCreator._instances

    def delete_checkbox(self: object):
        """This function deletes the given class object.

        Args:
            self (object): Instance of the class that will be deleted.
        """
        self.checkbutton.destroy()


class InputLineCreator:
    instances_dict = {
        'testcases': {
            'col1': [],
            'col2': [],
            'row': 1
        },
        'calc_value': {
            'col1': [],
            'col2': [],
            'row': 1
        }
    }

    def __init__(self, frame, input_type) -> None:
        self.text_var_col1 = tk.StringVar()
        self.text_var_col2 = tk.StringVar()
        # Create input for the left column
        if input_type == 'testcases':
            self.input_line_col1 = tk.Entry(frame,
                                            textvariable=self.text_var_col1,
                                            width=60)
        if input_type == 'calc_value':
            functions = list(CalcFunctions.getFunctionDict())
            self.input_line_col1 = ttk.Combobox(frame,
                                                textvariable=self.text_var_col1,
                                                values=functions, width=57)
        self.input_line_col1.grid(column=0,
                                  row=InputLineCreator.instances_dict[input_type]['row'],
                                  sticky='we', padx=10, pady=(0, 5))
        InputLineCreator.instances_dict[input_type]['col1'].append(self)
        # Create input for the righr column
        self.input_line_col2 = tk.Entry(frame, textvariable=self.text_var_col2,
                                        width=60)
        self.input_line_col2.grid(column=1,
                                  row=InputLineCreator.instances_dict[input_type]['row'],
                                  sticky='we', padx=10, pady=(0, 5))
        InputLineCreator.instances_dict[input_type]['col2'].append(self)
        # Increase the row position by 1
        InputLineCreator.instances_dict[input_type]['row'] += 1

    def get_all_instances(input_type) -> list:
        """This function returns a list that contains the entry line pairs of
           given input type of the class as tupels.

        Returns:
            list: A list of all instances of the class that were instantiated.
        """
        col1 = InputLineCreator.instances_dict[input_type]['col1']
        col2 = InputLineCreator.instances_dict[input_type]['col2']
        return list(zip(col1, col2))

    def delete_entry_line(self: object, col: str):
        """This function deletes the given class object.

        Args:
            self (object): Instance of the class that will be deleted.
        """
        if col == 'col1':
            self.input_line_col1.destroy()
        elif col == 'col2':
            self.input_line_col2.destroy()

    def delete_obj_instances_dict(input_type, col, obj):
        InputLineCreator.instances_dict[input_type][col].remove(obj)

    def get_text(self, col):
        if col == 'col1':
            return self.text_var_col1.get()
        elif col == 'col2':
            return self.text_var_col2.get()

    def insert_text_entry_obj(self: object, col: str, text: str):
        if col == 'col1':
            self.input_line_col1.insert(0, text)
        if col == 'col2':
            self.input_line_col2.insert(0, text)

    def clean_up_objects():
        """This function removes all objects from the instances dict and sets
           the row number to 1.
        """
        InputLineCreator.instances_dict['testcases']['col1'] = []
        InputLineCreator.instances_dict['testcases']['col2'] = []
        InputLineCreator.instances_dict['testcases']['row'] = 1
        InputLineCreator.instances_dict['calc_value']['col1'] = []
        InputLineCreator.instances_dict['calc_value']['col2'] = []
        InputLineCreator.instances_dict['calc_value']['row'] = 1
