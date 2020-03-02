#导入tkinter模块
import tkinter as t

#创建主窗口对象
root = t.Tk()

#调整窗口大小
#root.geometry('900x600')
root.minsize(900,600)

#创建组件
btn = t.Button(root,text='尺寸')

btn2 = t.Button(root,text='颜色',bg='blue',font=('黑体',30))

btn3 = t.Button(root,text='锚点',anchor='sw',font=('楷体',100,'italic'),fg='grey',state='normal',underline=3)

btn4 = t.Button(root,text='三D',relief='ridge',state='active')

btn5 = t.Button(root,text='位图',bitmap='gray25',underline=1)

btn6 = t.Button(root,text='鼠标',cursor='heart',underline=2)


#组件摆放
btn.pack()

btn2.place(x=100,y=100,width=100,height=100)

btn3.pack(ipadx=100,ipady=100)

btn4.pack(ipadx=20,ipady=20)

btn5.pack(ipadx=20,ipady=20)

btn6.pack(ipadx=20,ipady=20)


#将主窗口加入消息循环
root.mainloop()
