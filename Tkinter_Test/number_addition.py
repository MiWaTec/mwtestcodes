import tkinter as tk

def addiere():
    zahl1 = float(entry1.get())
    zahl2 = float(entry2.get())
    summe = zahl1 + zahl2
    label.config(text="Die Summe ist: " + str(summe))

# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Zahlen Addieren")

# Erstelle Eingabefelder
label1 = tk.Label(root, text="Zahl 1:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Zahl 2:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Erstelle Schaltfläche zum Addieren
button = tk.Button(root, text="Addieren", command=addiere)
button.pack()

# Erstelle Ausgabelabel
label = tk.Label(root, text="")
label.pack()

# Starte die Hauptereignisschleife
root.mainloop()
