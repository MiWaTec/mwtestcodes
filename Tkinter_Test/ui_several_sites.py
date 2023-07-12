import tkinter as tk
from tkinter import messagebox

def open_file():
    messagebox.showinfo("Datei", "Datei öffnen")

def save_file():
    messagebox.showinfo("Datei", "Datei speichern")

def setup():
    messagebox.showinfo("Setup", "Einstellungen ändern")

def help():
    messagebox.showinfo("Hilfe", "Hilfe aufrufen")

# Hauptfenster erstellen
root = tk.Tk()

# Funktionen für Menübefehle

# Menüleiste erstellen
menubar = tk.Menu(root)

# Datei-Menü
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Öffnen", command=open_file)
file_menu.add_command(label="Speichern", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Beenden", command=root.quit)
menubar.add_cascade(label="Datei", menu=file_menu)

# Setup-Menü
setup_menu = tk.Menu(menubar, tearoff=0)
setup_menu.add_command(label="Einstellungen", command=setup)
menubar.add_cascade(label="Setup", menu=setup_menu)

# Hilfe-Menü
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="Hilfe anzeigen", command=help)
menubar.add_cascade(label="Hilfe", menu=help_menu)

# Menüleiste dem Hauptfenster hinzufügen
root.config(menu=menubar)

# Hauptfenster starten
root.mainloop()
