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

lst = tk.Listbox(root, height=6)
lst.pack()

txt = tk.Text(root, height=6)
txt.pack()

def txt_write(s):
    txt.insert("end", s+ "\n")
    txt.see("end")
def do_add():
    name = ent.get().strip()
    cat = cmb.get() or "-"
    mark = "*" if flag.get() else "·"
    if not name:
        log_write("! Enter a name first")
        return
    item = f"{mark} {name} [{cat}]"
    lst.insert("end", item)
    log_write(f"+ {item}")
    ent.delete(0, "end")

def do_del():
    sel = lst.curselection()
    if not sel:
        log_write("! Nothing selected")
        return
    item = lst.get(sel[0])
    lst.delete(sel[0])
    log_write(f"- {item}")

def do_clr():
    lst.delete(0, "end")
    log.delete("1.0", "end")
    log_write("~ cleared")

btn_add.config(command=do_add)
btn_del.config(command=do_del)
btn_clr.config(command=do_clr)


root.mainloop()

