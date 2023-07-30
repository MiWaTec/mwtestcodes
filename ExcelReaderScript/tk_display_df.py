import tkinter as tk
from tkinter import ttk
import pandas as pd

def display_dataframe_as_table(dataframe):
    root = tk.Tk()
    root.title("DataFrame Table")

    # Create a Treeview widget
    tree = ttk.Treeview(root)

    # Set up columns
    tree["columns"] = list(dataframe.columns)
    for column in dataframe.columns:
        tree.column(column, anchor="center")
        tree.heading(column, text=column)

    # Insert data from DataFrame into the Treeview
    for index, row in dataframe.iterrows():
        tree.insert("", "end", values=list(row))

    # Add a vertical scrollbar
    scroll_y = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll_y.set)

    # Pack the widgets
    tree.pack(side="left", fill="both", expand=True)
    scroll_y.pack(side="right", fill="y")

    root.mainloop()

if __name__ == "__main__":
    # Example DataFrame (replace this with your own DataFrame)
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David"]
    }
    df = pd.DataFrame(data)

    # Display the DataFrame as a table using tkinter
    display_dataframe_as_table(df)