import tkinter as t

#创建主窗体对象
root = t.Tk() 

#设置窗体大小
root.minsize(900,600)


#创建组件
entry = t.Entry(width=50,bg='grey',fg='yellow')
entry.pack()

#密码
password = t.Entry(width=50,bg='grey',fg='yellow',show='*')
password.pack()

#将主窗体加入消息循环
root.mainloop()
