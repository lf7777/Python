import tkinter as t

#创建主窗体对象
root = t.Tk() 

#设置窗体大小
root.minsize(900,600)


#设置变量内容
text1 = t.StringVar()
text1.set('同意此协议')

#设置勾选的值
result = t.IntVar()

#勾选函数
def func():
    print(result.get())


#创建组件
#ctn = t.Checkbutton(root,text='同意此协议')
ctn = t.Checkbutton(root,textvariable=text1,variable=result,command=func)



#组件摆放
ctn.pack()



#将主窗体加入消息循环
root.mainloop()
