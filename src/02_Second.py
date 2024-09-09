from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        mensaje.set("Mensaje")
    except ValueError:
        pass
    
root = Tk()
root.title("Mensaje en una etiqueta")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mensaje = StringVar()
ttk.Label(mainframe, text="Etiqueta").grid(column=1, row=2, sticky=E)

ttk.Button(mainframe, text="Mensaje", command=calculate).grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()

root.bind("<Return>", calculate)
