import tkinter as t

#创建主窗体对象
root = t.Tk() 

#设置窗体大小
root.minsize(900,600)


#创建frame框架组件
frame1 = t.Frame(bg='grey',width=800,height=200)
frame1.pack()


frame2 = t.Frame(bg='blue',width=800,height=200)
frame2.pack()

#创建按钮组件
btn1 = t.Button(frame1,text='按钮1')
btn2 = t.Button(frame1,text='按钮2')
btn3 = t.Button(frame1,text='按钮3')

btn1.pack(side='left',padx=0)
btn2.pack(side='left',padx=50)
btn3.pack(side='left',padx=50)




#将主窗体加入消息循环
root.mainloop()
