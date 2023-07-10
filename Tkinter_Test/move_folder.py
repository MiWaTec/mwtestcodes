import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import time
import threading

def create_folder(directory):
    try:
        os.makedirs(directory)
        messagebox.showinfo("Ordner erstellt", f"Der Ordner '{directory}' wurde erstellt.")
    except FileExistsError:
        messagebox.showinfo("Ordner existiert", f"Der Ordner '{directory}' existiert bereits.")

def move_file(source_file, destination_folder):
    try:
        shutil.move(source_file, destination_folder)
        messagebox.showinfo("Datei verschoben", f"Die Datei '{source_file}' wurde nach '{destination_folder}' verschoben.")
    except FileNotFoundError:
        messagebox.showinfo("Fehler", "Die Datei wurde nicht gefunden.")
    except shutil.Error as e:
        messagebox.showinfo("Fehler", f"Fehler beim Verschieben der Datei: {e}")

def browse_file():
    file_path = filedialog.askopenfilename()
    entry_file.delete(0, tk.END)
    entry_file.insert(tk.END, file_path)

def browse_folder():
    destination_folder = filedialog.askdirectory()
    entry_folder.delete(0, tk.END)
    entry_folder.insert(tk.END, destination_folder)

def move_file_handler():
    file_path = entry_file.get()
    destination_folder = entry_folder.get()

    if file_path and destination_folder:
        create_folder(destination_folder)

        progress_bar.start(5)  # Starte den Ladebalken mit einer Geschwindigkeit von 5 Einheiten

        # Führe das Verschieben der Datei in einem separaten Thread aus
        move_thread = threading.Thread(target=move_file_thread, args=(file_path, destination_folder))
        move_thread.start()

    else:
        messagebox.showinfo("Fehler", "Bitte wähle eine Datei und einen Zielordner aus.")

def move_file_thread(file_path, destination_folder):
    move_file(file_path, destination_folder)
    time.sleep(5)  # Warte 5 Sekunden nach dem Verschieben der Datei

    # Beende den Ladebalken
    window.after(0, progress_bar.stop)

# Tkinter GUI erstellen
window = tk.Tk()
window.title("Datei verschieben")

# Hintergrundbild
background_image = tk.PhotoImage(file="sonnenuntergang.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Dateiauswahl
frame_file = tk.Frame(window)
frame_file.pack(pady=10)
label_file = tk.Label(frame_file, text="Datei:")
label_file.pack(side=tk.LEFT)
entry_file = tk.Entry(frame_file, width=50)
entry_file.pack(side=tk.LEFT, padx=10)
button_browse_file = tk.Button(frame_file, text="Durchsuchen", command=browse_file)
button_browse_file.pack(side=tk.LEFT)

# Zielordnerauswahl
frame_folder = tk.Frame(window)
frame_folder.pack(pady=10)
label_folder = tk.Label(frame_folder, text="Zielordner:")
label_folder.pack(side=tk.LEFT)
entry_folder = tk.Entry(frame_folder, width=50)
entry_folder.pack(side=tk.LEFT, padx=10)
button_browse_folder = tk.Button(frame_folder, text="Durchsuchen", command=browse_folder)
button_browse_folder.pack(side=tk.LEFT)

# Button zum Verschieben der Datei
button_move_file = tk.Button(window, text="Datei verschieben", command=move_file_handler)
button_move_file.pack(pady=10)

# Ladebalken
progress_bar = ttk.Progressbar(window, mode='determinate', length=200)
progress_bar.pack(pady=10)

# Tkinter GUI starten
window.mainloop()
