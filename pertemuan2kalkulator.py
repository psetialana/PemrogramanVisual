import tkinter as tk

def coba(val):
    if (v.get()=="0"):
        v.set("")
    elif (val=="+"):
        hasil = int(v.get())
        v.set("")
    elif (val=="="):
        hasil = hasil + int(v.get())
        v.set(str(hasil))
    else:
        v.set(v.get()+val)


master = tk.Tk()
master.title("kalkulator sederhana")
master.geometry("200x200")

v = tk.StringVar()
inputHasil = tk.Entry(master, text=v)
inputHasil.grid(row=0, column=0, columnspan=3)
v.set("0")

tk.Button(master, text="7", command=lambda:coba("7")).grid(row=1,column=0)
tk.Button(master, text="8", command=lambda:coba("8")).grid(row=1,column=1)
tk.Button(master, text="9").grid(row=1,column=2)
tk.Button(master, text="4").grid(row=2,column=0)
tk.Button(master, text="5").grid(row=2,column=1)
tk.Button(master, text="6").grid(row=2,column=2)
tk.Button(master, text="1").grid(row=3,column=0)
tk.Button(master, text="2").grid(row=3,column=1)
tk.Button(master, text="3").grid(row=3,column=2)
tk.Button(master, text="0").grid(row=4,column=0)
tk.Button(master, text="=", command=lambda:coba("=")).grid(row=4,column=1)
tk.Button(master, text="+", command=lambda:coba("+")).grid(row=4,column=2)
tk.Button(master, text="x").grid(row=5,column=0)
tk.Button(master, text=":").grid(row=5,column=1)
tk.Button(master, text="-").grid(row=5,column=2)


tk.mainloop()