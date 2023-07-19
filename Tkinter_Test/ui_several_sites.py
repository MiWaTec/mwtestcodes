import tkinter as tk
from tkinter import messagebox

class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("UI mit Menübar")

        # Menüleiste erstellen
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Datei-Menü
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Seite 1", command=self.open_page1)
        file_menu.add_command(label="Seite 2", command=self.open_page2)
        file_menu.add_command(label="Seite 3", command=self.open_page3)
        file_menu.add_separator()
        file_menu.add_command(label="Beenden", command=self.root.quit)
        menubar.add_cascade(label="Datei", menu=file_menu)

        # Seiten-Label
        self.page_label = tk.Label(self.root, text="Willkommen zur Startseite", font=("Helvetica", 18))
        self.page_label.pack(pady=50)

    def open_page1(self):
        self.page_label.config(text="Seite 1\nNummerierung: 1")

    def open_page2(self):
        self.page_label.config(text="Seite 2\nNummerierung: 2")

    def open_page3(self):
        self.page_label.config(text="Seite 3\nNummerierung: 3")

    def run(self):
        self.root.mainloop()

# UI starten
ui = UI()
ui.run()
