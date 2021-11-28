from matplotlib import pyplot as plt

x =[1,2,3,5,6]
y=[2,3,4,6,7]
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
fig1 = plt.figure(figsize=(5,5))
plt.plot(x,y)
plt.title(u'看看吧')
plt.xlabel('time')
plt.ylabel('height')
plt.show()