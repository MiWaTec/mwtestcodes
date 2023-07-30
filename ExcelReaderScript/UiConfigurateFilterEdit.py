import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
from evaluate_excel import read_filter_json


def initialize_page_edit(window):
    page = tk.Frame(window)
    page.grid(row=0, column=0, sticky='nsew')
