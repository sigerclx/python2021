from tkinter import *
from tkinter import ttk  # 导入ttk模块，因为下拉菜单控件在ttk中
root = Tk()  # 创建窗口对象的背景色


# 创建下拉列表1
cmb1 = ttk.Combobox(root)
cmb1.pack()
# 设置下拉菜单中的值
cmb1['value'] = ('dasla','balster','海康威视')
# 设置默认值，即默认下拉框中的内容
cmb1.current(2)
# 默认值中的内容为索引，从0开始


# 创建下拉列表2
cmb2 = ttk.Combobox(root)
cmb2.pack()
# 设置下拉菜单中的值
cmb2['value'] = ('500w','200w','1200w','1800w')
# 设置默认值，即默认下拉框中的内容
cmb2.current(2)
# 默认值中的内容为索引，从0开始

text = Text(root)
text.insert('insert','相机是xxx物距')
text.insert('insert',' =56mm')
text.pack()


root.mainloop()  # 进入消息循环