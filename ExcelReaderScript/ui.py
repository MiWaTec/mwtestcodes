import tkinter as tk
import UiConfigurateFilter
import UiMainMenu
import UiSettingMenu


def menubar_go_to_mainmenu():
    UiSettingMenu.unload_settings()
    UiMainMenu.unload_available_settings()
    UiMainMenu.initialize_page_main_menu(window)
    UiMainMenu.load_available_settings('default_settings.json', window)


def menubar_go_to_setup():
    UiConfigurateFilter.initialize_page_configurate_filter(window)


# Create UI window
window = tk.Tk()
# Create title of the window
window.title('Test Result Calculator')
# Set size of the window
window.minsize(width=555, height=200)
window.resizable(False, False)


# Create Menubar
menubar = tk.Menu(window)
window.config(menu=menubar)
# File Menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Main', menu=file_menu)
file_menu.add_command(label='Main menu', command=menubar_go_to_mainmenu)
# Setup
setup_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Setup', menu=setup_menu)
setup_menu.add_command(label='Configurate filter', command=menubar_go_to_setup)


# Display main menu
UiMainMenu.initialize_page_main_menu(window)
UiMainMenu.load_available_settings('default_settings.json', window)

# Loop for waiting for interaction of the user
window.mainloop()
