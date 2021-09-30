import tkinter as tk

root = tk.Tk()
root.resizable(False, False)
root.title("Text Widget Example")

label1 = tk.Label(
    root,
    text='Silahkan masukan alamat Anda :',
    fg="black"
)

label1.pack(
    ipadx=10,
    ipady=10,
    fill='x'
)

text = tk.Text(root, height=8)
text.pack()


root.mainloop()