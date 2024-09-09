from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        mensaje.set("Mensaje")
    except ValueError:
        pass

root = Tk()
root.geometry("300x100")
root.title("Mensaje en una etiqueta")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mensaje = StringVar()
ttk.Label(mainframe, textvariable=mensaje ).grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=1, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", calculate)

root.mainloop()