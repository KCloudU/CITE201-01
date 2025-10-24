import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter design")

label= tk.Label(root, text="To-Do")
label.pack()

entry = tk.Entry(root)
entry.pack()

cmb = ttk.Combobox(root, values=("A","B","C"), state ="readonly")
cmb.pack()

chk_var = tk.BooleanVar()
chk = tk.Checkbutton(root, text="Important", variable=chk_var)
chk.pack()

btn_add = tk.Button(root, text="Add")
btn_add.pack()

btn_del = tk.Button(root, text="Delete Selected")
btn_del.pack()

btn_clr = tk.Button(root, text="Clear All")
btn_clr.pack()

lst = tk.Listbox(root)
lst.pack()

txt = tk.Text(root)
txt.pack()

root.mainloop()

