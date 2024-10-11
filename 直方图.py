import numpy as np  # 导入numpy库，用于处理数组数据
import matplotlib.pyplot as plt  # 导入matplotlib库，用于绘制图形

# 设置字体和负号显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为SimHei以支持中文显示
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义电影名称和票房数据
movie = ['新蝙蝠侠', '狙击手', '奇迹笨小孩']  # 电影名称列表
real_day1 = np.array([4053, 2548, 1543])  # 第一天的票房数据
real_day2 = np.array([7840, 4013, 2421])  # 第二天的票房数据
real_day3 = np.array([8080, 3673, 1342])  # 第三天的票房数据

# 确定每一天的票房数据在水平柱状图中的起始位置
left_day2 = real_day1  # 第二天的票房数据从第一天的票房数据结束位置开始
left_day3 = real_day1 + real_day2  # 第三天的票房数据从前两天的票房数据结束位置开始

# 设置柱状图的高度
height = 0.2  # 每个柱状图的高度

# 绘制水平柱状图
plt.barh(movie, real_day1, height=height)  # 绘制第一天的票房数据
plt.barh(movie, real_day2, left=left_day2, height=height)  # 绘制第二天的票房数据
plt.barh(movie, real_day3, left=left_day3, height=height)  # 绘制第三天的票房数据

# 设置数值文本，显示在每个柱状图的末端
sum_data = real_day1 + real_day2 + real_day3  # 计算每部电影的总票房
for i in range(len(movie)):
    plt.text(sum_data[i], movie[i], sum_data[i], va="center", ha="left")  # 在每个柱状图的末端显示总票房

# 设置图表标题和轴标签
plt.title("各电影票房")  # 设置图表标题
plt.xlabel("票房(万)")  # 设置x轴标签
plt.ylabel("电影名称")  # 设置y轴标签

# 显示图表

plt.show()  # 显示绘制的图表