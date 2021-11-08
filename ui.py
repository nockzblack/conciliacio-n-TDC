from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Conciliación TDC")
root.geometry('700x500+200+200')
root.resizable(False, False)

auxFrame = ttk.Frame(root, padding=10)
auxFrame.grid()


ttk.Button(auxFrame, text="Agregar Tarjeta").grid(column=0, row=0)
ttk.Button(auxFrame, text="Agregar Info from Excel").grid(column=1, row=1)
ttk.Button(auxFrame, text="Salir", command=root.destroy).grid(
    column=0, row=4)
root.mainloop()
