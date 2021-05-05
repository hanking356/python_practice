from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text = 'Hello')
label.pack()

# Label을 수정하려면 config를 사용하면 된다.
label.config(text = 'The label is changed')

root.mainloop()