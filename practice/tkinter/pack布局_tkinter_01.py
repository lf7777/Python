import tkinter as t

root = t.Tk()    #创建主窗口对象           

root.minsize(300,300)    #设置窗口最小的大小

btn = t.Button(root,text='文件')    #创建按钮对象,还在内存中
btn1 = t.Button(root,text='编辑')    #创建按钮对象,还在内存中
btn2 = t.Button(root,text='首选项')    #创建按钮对象,还在内存中

btn.pack(ipadx=30,fill='x')    #让cpu运行按钮到主窗口上
btn1.pack(side='left',ipady=10,padx=20,fill='y')    #让cpu运行按钮到主窗口上
btn2.pack(expand='yes',fill='both')    #让cpu运行按钮到主窗口上

root.mainloop()    #将主窗口加入消息循环
