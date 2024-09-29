import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号“-”显示异常

countries = ['挪威', '德国', '中国', '美国', '瑞典']
total_medal = np.array([16 + 8 + 13, 12 + 10 + 5, 9 + 4 + 2, 8 + 10 + 7, 8 + 5 + 5])

width = 0.3  # 绘图

plt.barh(countries, total_medal, color='steelblue', height=width)  # 设置y轴标签，图例和文本值

plt.xlabel('奖牌数')
plt.legend(loc='upper right')

for i in range(len(countries)):
    max_x = total_medal[i]
    plt.text(max_x, countries[i], max_x, va="center", ha="left")

plt.show()
