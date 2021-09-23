import tkinter as tk

root = tk.Tk()
root.title('Tkinter place Geometry Manager')
root.geometry("500x500")

# label 1
label1 = tk.Label(
    root,
    text="Absolute placement",
    bg='red',
    fg='white'
)

label1.place(x=10, y=5)

# label 2
label2 = tk.Label(
    root,
    text="Relative placement",
    bg='blue',
    fg='white'
)

label2.place(relx=0, rely=0.2, relwidth=1, relheight=0.5)

root.mainloop()