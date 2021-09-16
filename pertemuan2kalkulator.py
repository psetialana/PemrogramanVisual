import tkinter as tk

hasil = 0.0
operator = ""

def angka(val):
    if (v.get()=="0"):
        v.set(val)
    else:
        v.set(v.get()+val)

def operasi(op):
    global operator
    global hasil
    if (op=="="):
        if (operator=="+"):
            hasil = hasil + float(v.get())
            v.set(str(hasil))
        if (operator=="x"):
            hasil = hasil * float(v.get())
            v.set(str(hasil))
        if (operator=="-"):
            hasil = hasil - float(v.get())
            v.set(str(hasil))
        if (operator==":"):
            hasil = hasil / float(v.get())
            v.set(str(hasil))
        operator = ""
    else:
        hasil = float(v.get())
        operator = op
        v.set("0")


master = tk.Tk()
master.title("kalkulator sederhana")
master.geometry("200x200")

v = tk.StringVar()
inputHasil = tk.Entry(master, text=v)
inputHasil.grid(row=0, column=0, columnspan=3)
v.set("0")

tk.Button(master, text="7", command=lambda:angka("7")).grid(row=1,column=0)
tk.Button(master, text="8", command=lambda:angka("8")).grid(row=1,column=1)
tk.Button(master, text="9", command=lambda:angka("9")).grid(row=1,column=2)
tk.Button(master, text="4", command=lambda:angka("4")).grid(row=2,column=0)
tk.Button(master, text="5", command=lambda:angka("5")).grid(row=2,column=1)
tk.Button(master, text="6", command=lambda:angka("6")).grid(row=2,column=2)
tk.Button(master, text="1", command=lambda:angka("1")).grid(row=3,column=0)
tk.Button(master, text="2", command=lambda:angka("2")).grid(row=3,column=1)
tk.Button(master, text="3", command=lambda:angka("3")).grid(row=3,column=2)
tk.Button(master, text="0", command=lambda:angka("0")).grid(row=4,column=0)
tk.Button(master, text="=", command=lambda:operasi("=")).grid(row=4,column=1)
tk.Button(master, text="+", command=lambda:operasi("+")).grid(row=4,column=2)
tk.Button(master, text="x", command=lambda:operasi("x")).grid(row=5,column=0)
tk.Button(master, text=":", command=lambda:operasi(":")).grid(row=5,column=1)
tk.Button(master, text="-", command=lambda:operasi("-")).grid(row=5,column=2)


tk.mainloop()