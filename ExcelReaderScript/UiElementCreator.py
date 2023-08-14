import tkinter as tk
import UiSettingMenu
from evaluate_excel import save_filter


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
