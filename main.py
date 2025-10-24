import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter design")

label= tk.Label(root, text="To-Do")
label.pack()

entry = tk.Entry(root)
entry.pack()

btn =tk.Button(root,text="Button")
btn.pack()

chk_var = tk.BooleanVar()
chk = tk.Checkbutton(root, text="Checkbutton", variable=chk_var)
chk.pack()

lst = tk.Listbox(root)
lst.pack()

cmb= ttk.Combobox(root, values=("tst1","tst2","tst3"), state="readonly")
cmb.pack()

txt = tk.Text(root)
txt.pack()

root.mainloop()

