import tkinter as t

root = t.Tk()

root.minsize(900,600)

#步骤1:创建主菜单
menu1 = t.Menu(root)


#步骤2:创建子菜单
#步骤3:将子菜单加入主菜单
childmenu1 = t.Menu(menu1,tearoff=0)

#为子菜单添加功能
childmenu1.add_command(label='打开文件')
childmenu1.add_separator()
childmenu1.add_command(label='保存文件')
childmenu1.add_command(label='另存为文件')

menu1.add_cascade(label='文件',menu=childmenu1)



childmenu2 = t.Menu(menu1)

menu1.add_cascade(label='编辑',menu=childmenu2)


#步骤4:将主菜单加入界面
root.config(menu=menu1)



root.mainloop()
