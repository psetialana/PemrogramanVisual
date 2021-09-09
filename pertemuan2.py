import tkinter as tk

def createName():
    nama = inputNama.get()
    alamat = inputAlamat.get()
    tk.Label(master, text="Nama Anda: " + nama).grid(row=4, column=1, sticky=tk.W)
    tk.Label(master, text="Alamat Anda: " + alamat).grid(row=5, column=1, sticky=tk.W)

master = tk.Tk()
master.title("First UI Code")
master.geometry("500x500")

inputNama = tk.Entry(master)
inputAlamat = tk.Entry(master)

tk.Label(master, text="Nama : ").grid(row=0, column=0)
tk.Label(master, text="Alamat : ").grid(row=1, column=0)
inputNama.grid(row=0, column=1)
inputAlamat.grid(row=1, column=1)
tk.Button(master, text='Tampilkan', command=createName).grid(row=0, column=2)

tk.mainloop()