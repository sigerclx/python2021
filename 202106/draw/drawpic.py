#!/usr/bin/env python
# encoding: utf-8
"""
@Company：华中科技大学电气学院聚变与等离子研究所
@version: V1.0
@author: Victor
@contact: 1650996069@qq.com or yexin@hust.edu.cn 2018--2020
@software: PyCharm
@file: PlotByMatlibplot.py
@time: 2018/9/16 15:18
@Desc：讲解一些matlibplot的使用
"""

# 导入相关模块
import matplotlib.pyplot as plt
import numpy as np

##############################画一个简单的图形#####################################
# 首先通过 np.linspace 方式生成 x，
# 它包含了 50 个元素的数组，这 50 个元素均匀的分布在 [0, 2*pi] 的区间上。然后通过 np.sin(x) 生成 y。

x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)
# 有了 x 和 y 数据之后，我们通过 plt.plot(x, y) 来画出图形，并通过 plt.show() 来显示。
plt.plot(x, y)
plt.show()
##############################画一个简单的图形#####################################
# 首先通过 np.linspace 方式生成 x，
# 它包含了 50 个元素的数组，这 50 个元素均匀的分布在 [0, 2*pi] 的区间上。然后通过 np.sin(x) 生成 y。

x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)
# 有了 x 和 y 数据之后，我们通过 plt.plot(x, y) 来画出图形，并通过 plt.show() 来显示。
plt.plot(x, y)
plt.show()
#################################在一个画板里绘制多个图############################
plt.plot(x, y)
plt.plot(x, y ** 3)
plt.show()

# 绘制出图形之后，我们可以自己调整更多的样式，比如颜色、点、线。
plt.plot(x, y, 'y*-')
plt.plot(x, y ** 3, 'm--')  # 设置样式时，就是增加了一个字符串参数，比如 'y*-' ，其中 y 表示黄色，* 表示 星标的点，- 表示实线。
plt.show()

###############################设置 figure和标题以及其他图列，注释属性######################################
# 可以认为Matplotlib绘制的图形都在一个默认的 figure 中，当然了，

# 你可以自己创建 figure，好处就是可以控制更多的参数，常见的就是控制图形的大小，这里创建一个 figure，设置大小为 (8, 4)

plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.plot(x, y * 2)
plt.title("cos(x) & cos(x)*2")

# 设置坐标轴的刻度，范围
plt.xlim((0, 2 * np.pi))
plt.ylim((-2, 2))
plt.xlabel('X')
plt.ylabel('Y')  # 通过 xlim 和 ylim 来设限定轴的范围，通过 xlabel 和 ylabel 来设置轴的名称

# 我们也可以通过 xticks 和 yticks 来设置轴的刻度
# plt.xticks((0, np.pi * 0.5, np.pi, np.pi * 1.5, np.pi * 2))

###设置 label 和 legend
# 设置 label 和 legend 的目的就是为了区分出每个数据对应的图形名称。
plt.plot(x, y, label="cos(x)")
plt.plot(x, -y * 2, label="2cos(x)")
# plt.legend()
plt.legend(loc='best')

#####添加注释######
# 需要对特定的点进行标注，我们可以使用 plt.annotate 函数来实现。
#
# 这里我们要标注的点是 (x0, y0) = (π, 0)。
#
# 我们也可以使用 plt.text 函数来添加注释。
x0 = np.pi
y0 = 0

# 画出标注点
plt.scatter(x0, y0, s=50)
plt.annotate('sin(np.pi)=%s' % y0, xy=(np.pi, 0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
# 对于 annotate 函数的参数，做一个简单解释：
#
# 'sin(np.pi)=%s' % y0 代表标注的内容，可以通过字符串 %s 将 y0 的值传入字符串；
# 参数 xycoords='data' 是说基于数据的值来选位置;
# xytext=(+30, -30) 和 textcoords='offset points' 表示对于标注位置的描述 和 xy 偏差值，即标注位置是 xy 位置向右移动 30，向下移动30；
# arrowprops 是对图中箭头类型和箭头弧度的设置，需要用 dict 形式传入。

plt.text(0.5, -0.25, "sin(np.pi) = 0", fontdict={'size': 18, 'color': 'r'})
plt.show()
#画子图
##############################画一个简单的图形#####################################
# 首先通过 np.linspace 方式生成 x，
# 它包含了 50 个元素的数组，这 100 个元素均匀的分布在 [0, 50] 的区间上

x = np.linspace(0, 50, 100)

############################使用子图##############################################
# 将多张子图展示在一起，可以使用 subplot() 实现。即在调用 plot() 函数之前需要先调用 subplot() 函数。
# 该函数的第一个参数代表子图的总行数，第二个参数代表子图的总列数，第三个参数代表活跃区域。
ax1 = plt.subplot(2, 2, 1)  # （行，列，活跃区）
plt.plot(x, np.sin(x), 'r')

ax2 = plt.subplot(2, 2, 2, sharey=ax1)  # 与 ax1 共享y轴
plt.plot(x, 2 * np.cos(x), 'g')

ax3 = plt.subplot(2, 2, 3)
plt.plot(x, np.tan(x), 'b')

ax4 = plt.subplot(2, 2, 4, sharey=ax3)  # 与 ax3 共享y轴
plt.plot(x, 2 * np.sin(x), 'y')
# subplot(2, 2, x) 表示将图像窗口分为 2 行 2 列。x 表示当前子图所在的活跃区

plt.show()

############################调整子图大小的位置##################################
# 上面的每个子图的大小都是一样的。有时候我们需要不同大小的子图。比如将上面第一张子图完全放置在第一行，其他的子图都放在第二行。
ax1 = plt.subplot(2, 1, 1)  # （行，列，活跃区）
plt.plot(x, np.sin(x), 'r')

ax2 = plt.subplot(2, 3, 4)
plt.plot(x, 2 * np.sin(x), 'g')

ax3 = plt.subplot(2, 3, 5, sharey=ax2)
plt.plot(x, np.cos(x), 'b')

ax4 = plt.subplot(2, 3, 6, sharey=ax2)
plt.plot(x, 2 * np.cos(x), 'y')
# plt.subplot(2, 1, 1) 将图像窗口分为了 2 行 1 列, 当前活跃区为 1。

# 使用 plt.subplot(2, 3, 4) 将整个图像窗口分为 2 行 3 列, 当前活跃区为 4。
#
# 解释下为什么活跃区为 4，因为上一步中使用 plt.subplot(2, 1, 1) 将整个图像窗口分为 2 行 1 列, 第1个小图占用了第1个位置,
# 也就是整个第1行. 这一步中使用 plt.subplot(2, 3, 4) 将整个图像窗口分为 2 行 3 列,
# 于是整个图像窗口的第1行就变成了3列, 也就是成了3个位置, 于是第2行的第1个位置是整个图像窗口的第4个位置。
plt.show()

###############散点图###################
k = 500
x = np.random.rand(k)
y = np.random.rand(k)
size = np.random.rand(k) * 50  # 生成每个点的大小，每个数据点生成控制大小的数组 size
colour = np.arctan2(x, y)  # 生成每个点的颜色大小，每个数据点生成控制颜色的数组 colour
plt.scatter(x, y, s=size, c=colour)
plt.colorbar()  # 添加颜色栏

plt.show()
#####################柱状图#############

k = 10
x = np.arange(k)
y = np.random.rand(k)
plt.bar(x, y)  # 画出 x 和 y 的柱状图

# 增加数值
for x, y in zip(x, y):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
    # 通过
    # plt.text
    # 标注数值，设置参数
    # ha = 'center'
    # 横向居中对齐，设置
    # va = 'bottom'
    # 纵向底部（顶部）对齐

plt.show()
#####################柱状图#############

k = 10
x = np.arange(k)
y = np.random.rand(k)
plt.bar(x, y)  # 画出 x 和 y 的柱状图

# 增加数值
for x, y in zip(x, y):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
    # 通过
    # plt.text
    # 标注数值，设置参数
    # ha = 'center'
    # 横向居中对齐，设置
    # va = 'bottom'
    # 纵向底部（顶部）对齐

plt.show()
#####################柱状图#############

k = 10
x = np.arange(k)
y = np.random.rand(k)
plt.bar(x, y)  # 画出 x 和 y 的柱状图

# 增加数值
for x, y in zip(x, y):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
    # 通过
    # plt.text
    # 标注数值，设置参数
    # ha = 'center'
    # 横向居中对齐，设置
    # va = 'bottom'
    # 纵向底部（顶部）对齐

plt.show()
#####################柱状图#############

k = 10
x = np.arange(k)
y = np.random.rand(k)
plt.bar(x, y)  # 画出 x 和 y 的柱状图

# 增加数值
for x, y in zip(x, y):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
    # 通过
    # plt.text
    # 标注数值，设置参数
    # ha = 'center'
    # 横向居中对齐，设置
    # va = 'bottom'
    # 纵向底部（顶部）对齐

plt.show()
#####################柱状图#############

k = 10
x = np.arange(k)
y = np.random.rand(k)
plt.bar(x, y)  # 画出 x 和 y 的柱状图

# 增加数值
for x, y in zip(x, y):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
    # 通过
    # plt.text
    # 标注数值，设置参数
    # ha = 'center'
    # 横向居中对齐，设置
    # va = 'bottom'
    # 纵向底部（顶部）对齐

plt.show()
#####################柱状图#############

k = 10
x = np.arange(k)
y = np.random.rand(k)
plt.bar(x, y)  # 画出 x 和 y 的柱状图

# 增加数值
for x, y in zip(x, y):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
    # 通过
    # plt.text
    # 标注数值，设置参数
    # ha = 'center'
    # 横向居中对齐，设置
    # va = 'bottom'
    # 纵向底部（顶部）对齐

plt.show()
#####################柱状图#############

k = 10
x = np.arange(k)
y = np.random.rand(k)
plt.bar(x, y)  # 画出 x 和 y 的柱状图

# 增加数值
for x, y in zip(x, y):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
    # 通过
    # plt.text
    # 标注数值，设置参数
    # ha = 'center'
    # 横向居中对齐，设置
    # va = 'bottom'
    # 纵向底部（顶部）对齐

plt.show()
#####################柱状图#############

k = 10
x = np.arange(k)
y = np.random.rand(k)
plt.bar(x, y)  # 画出 x 和 y 的柱状图

# 增加数值
for x, y in zip(x, y):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
    # 通过
    # plt.text
    # 标注数值，设置参数
    # ha = 'center'
    # 横向居中对齐，设置
    # va = 'bottom'
    # 纵向底部（顶部）对齐

plt.show()
#####################柱状图#############

k = 10
x = np.arange(k)
y = np.random.rand(k)
plt.bar(x, y)  # 画出 x 和 y 的柱状图

# 增加数值
for x, y in zip(x, y):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
    # 通过
    # plt.text
    # 标注数值，设置参数
    # ha = 'center'
    # 横向居中对齐，设置
    # va = 'bottom'
    # 纵向底部（顶部）对齐

plt.show()
#####################柱状图#############

k = 10
x = np.arange(k)
y = np.random.rand(k)
plt.bar(x, y)  # 画出 x 和 y 的柱状图

# 增加数值
for x, y in zip(x, y):
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
    # 通过
    # plt.text
    # 标注数值，设置参数
    # ha = 'center'
    # 横向居中对齐，设置
    # va = 'bottom'
    # 纵向底部（顶部）对齐

plt.show()