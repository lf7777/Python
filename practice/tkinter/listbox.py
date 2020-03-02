import tkinter as t

root = t.Tk()

root.minsize(900,600)


names = ('啊','答复','大')
#将数据转换文 tkinter 可识别的 tkinter字符串变量
s = t.StringVar(value=names)

listbox = t.Listbox(root,listvariable=s)

listbox.pack()

root.mainloop()
