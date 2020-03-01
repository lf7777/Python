#导入tkinter模块
import tkinter as t

#创建主窗口对象
root = t.Tk()

#设定窗口最小大小
root.minsize(500,500)

#创建组件
btn7 = t.Button(root,text='7')
btn8 = t.Button(root,text='8')
btn9 = t.Button(root,text='9')
btn4 = t.Button(root,text='4')
btn5 = t.Button(root,text='5')
btn6 = t.Button(root,text='6')
btn1 = t.Button(root,text='1')
btn2 = t.Button(root,text='2')
btn3 = t.Button(root,text='3')
btn0 = t.Button(root,text='0')
btn_point = t.Button(root,text='.')
btn_add = t.Button(root,text='+')
btn_cut = t.Button(root,text='-')
btn_rid = t.Button(root,text='*')
btn_exc = t.Button(root,text='/')
btn_equ = t.Button(root,text='=')
btn_exit = t.Button(root,text='退出')

#组件摆放

#等于号 及 退出
btn_equ.grid(row=0,column=0,columnspan=3,ipadx=36)
btn_exit.grid(row=0,column=3)


#7 8 9 数字
btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btn_add.grid(row=1,column=3,ipadx=9)

#4 5 6 数字
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn_cut.grid(row=2,column=3,ipadx=10)

#1 2 3 数字
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btn_rid.grid(row=3,column=3,ipadx=9)

#0还有点
btn0.grid(row=4,column=0,columnspan=2,ipadx=18)
btn_point.grid(row=4,column=2,ipadx=2)
btn_exc.grid(row=4,column=3,ipadx=10)





#加入消息循环
root.mainloop()
