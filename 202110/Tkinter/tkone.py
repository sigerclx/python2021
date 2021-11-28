from tkinter import *
from tkinter import ttk  # 导入ttk模块，因为下拉菜单控件在ttk中
root = Tk()  # 创建窗口对象的背景色
# 创建两个列表
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb = Listbox(root)  # 创建两个列表组件
listb2 = Listbox(root)
for item in li:  # 第一个小部件插入数据
    listb.insert(0, item)

for item in movie:  # 第二个小部件插入数据
    listb2.insert(0, item)

listb.pack()  # 将小部件放置到主窗口中
listb2.pack()

# 创建下拉菜单
cmb = ttk.Combobox(root)
cmb.pack()
# 设置下拉菜单中的值
cmb['value'] = ('上海','北京','天津','广州')
# 设置默认值，即默认下拉框中的内容
cmb.current(2)
# 默认值中的内容为索引，从0开始


root.mainloop()  # 进入消息循环