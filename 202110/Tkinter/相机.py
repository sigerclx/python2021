from tkinter import *
from tkinter import ttk  # 导入ttk模块，因为下拉菜单控件在ttk中
from tkinter import messagebox
root = Tk()  # 创建窗口对象的背景色


def ButtonCallBack():
    pass
    #按钮功能
    #messagebox.showinfo("Hello Python", text1.get('0.0','end'))

L1 = Label(root, text="像元尺寸微米").grid(row=0,sticky=W)

E1 = Entry(root,text='像元尺寸微米',width=8).grid(row=0,column=1)

# 创建像素下拉列表2
Label(root, text="像素边长").grid(row=1,sticky=W)
cmb1 = ttk.Combobox(root,width=6)

# 设置下拉菜单中的值
cmb1['value'] = ('640','720','1024','1280','1440','1624','1920','2048','2448','3072','4096','5472')
cmb1.grid(row=1,column=1)
# 设置默认值，即默认下拉框中的内容
cmb1.current(0)

# 创建镜头下拉列表
Label(root, text="镜头选择").grid(row=2,sticky=W)
cmb2 = ttk.Combobox(root,width=6)

# 设置下拉菜单中的值
cmb2['value'] = ('6','8','12','25','50')
cmb2.grid(row=2,column=1)
# 设置默认值，即默认下拉框中的内容
cmb2.current(0)

# # 创建物距下拉列表
Label(root, text="物距设定").grid(row=3,sticky=W)
cmb3 = ttk.Combobox(root,width=6)

# 设置下拉菜单中的值
cmb3['value'] = ('100','150','250','300','400','600','800','900','1000')
cmb3.grid(row=3,column=1)
# 设置默认值，即默认下拉框中的内容
cmb3.current(0)

# 创建下拉菜单
L2 = Label(root, text="视野边长").grid(row=4,sticky=W)
E2 = Entry(root,text='像元尺寸微米',width=8).grid(row=4,column=1)

B = Button(root, text="计算", command=ButtonCallBack).grid(row=6)

root.mainloop()  # 进入消息循环