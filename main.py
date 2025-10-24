import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter design")

label= tk.Label(root, text="To-Do")
label.pack()

name_var = tk.StringVar()

entry = tk.Entry(root, textvariable=name_var)
entry.pack()

cmb = ttk.Combobox(root, values=("A","B","C"), state ="readonly")
cmb.pack()

flag = tk.BooleanVar(value=False)
chk = tk.Checkbutton(root, text="Important", variable=flag)
chk.pack()

btn_add = tk.Button(root, text="Add")
btn_add.pack()

btn_del = tk.Button(root, text="Delete Selected")
btn_del.pack()

btn_clr = tk.Button(root, text="Clear All")
btn_clr.pack()

lst = tk.Listbox(root, height=6)
lst.pack()

txt = tk.Text(root, height=6)
txt.pack()

def txt_write(s):
    txt.insert("end", s+ "\n")
    txt.see("end")
def do_add():
    name = name_var.get().strip()
    cat = cmb.get() or "-"
    mark = "*" if flag.get() else "·"
    if not name:
        txt_write("! Enter a name first")
        return
    item = f"{mark} {name} [{cat}]"
    lst.insert("end", item)
    txt_write(f"+ {item}")
    name_var.set("")

def do_del():
    sel = lst.curselection()
    if not sel:
        txt_write("! Nothing selected")
        return
    item = lst.get(sel[0])
    lst.delete(sel[0])
    txt_write(f"- {item}")

def do_clr():
    lst.delete(0, "end")
    txt.delete("1.0", "end")
    txt_write("~ cleared")

btn_add.config(command=do_add)
btn_del.config(command=do_del)
btn_clr.config(command=do_clr)


root.mainloop()

