import tkinter as t

#创建窗体对象
root = t.Tk()

root.minsize(900,600)

#创建组件
btn = t.Button(root,text='菜单')

#组件摆放
btn.place(relx = 0.1,rely = 0.2)


#加入消息循环
root.mainloop()
