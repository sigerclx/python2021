# matplotlib模块绘制直方图
import pandas as pd
import matplotlib.pyplot as plt
# 读入数据
# Titanic = pd.read_csv('titanic_train.csv')
# # 检查年龄是否有缺失
# any(Titanic.Age.isnull())
# # 不妨删除含有缺失年龄的观察
# Titanic.dropna(subset=['Age'], inplace=True)
#
x =[1,2,3,4,5]

Age = [20,15,16,8,14,16,8,14,3]

# 绘制直方图
# plt.hist(Age, # 指定绘图数据
#          bins = 5, # 指定直方图中条块的个数
#          color = 'steelblue', # 指定直方图的填充色
#          edgecolor = 'black' # 指定直方图的边框色
#          )
# # 添加x轴和y轴标签
# plt.xlabel('年龄')
# plt.ylabel('频数')
# # 添加标题
# plt.title('乘客年龄分布')
# # 显示图形
# plt.show()
X =[1,2,3]

A = [4,5,6]
B = [7,8,9]
x = list(range(len(A)))
print(x)
plt.bar(x,A,width=0.4,tick_label=X,fc='y')
for i in range(len(x)):
    x[i]+=0.4

plt.bar(x,B,width=0.4,fc='r')
plt.show()