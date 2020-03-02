import tkinter as t

root = t.Tk()

root.minsize(900,600)

lf = t.LabelFrame(root,text='LableFrame',font=('黑体,',20),bg='grey',width=300,height=300)

lf.grid()

btn = t.Button(lf,text='按钮')
btn.pack(side='left')

btn2 = t.Button(lf,text='按钮')
btn3 = t.Button(lf,text='按钮')
btn4 = t.Button(lf,text='按钮')
btn2.pack(side='left')
btn3.pack(side='left')
btn4.pack(side='left')

root.mainloop()
