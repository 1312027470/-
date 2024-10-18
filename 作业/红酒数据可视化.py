# 以红葡萄酒(winequality-red.csv)为对象，对其中数据进行如下初步处理：
# (1) 以分号为分隔符进行数据的读入。
# (2) 初识数据，给出数据的基本信息，包括字段名称、类型、字段个数、字段是否缺失以及数值数据的统计参数值(均值、个数、最大、最小、标准差等)。
# (3) 利用subplot绘制所有字段变量的箱线图、直方图、累计曲线图；绘制变量百分比饼图；分别绘制带注释和对角线矩阵的热力图，并观察各个字段的分布特点。
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取数据，以分号为分隔符
file_path = '作业\winequality-red.csv'
wine_data = pd.read_csv(file_path, delimiter=';')

# 1. 显示数据集的基本信息和前5行数据
print("数据集的基本信息：")
print(wine_data.info())
print("\n数据集的前5行：")
print(wine_data.head())

# 2. 数值型字段的统计信息
print("\n数值型字段的统计信息：")
print(wine_data.describe())

# 3. 数据可视化

# (1) 绘制各字段的箱线图
plt.figure(figsize=(20, 15))  # 设置图形大小
for i, column in enumerate(wine_data.columns[:-1]):
    plt.subplot(3, 4, i + 1)  # 创建子图
    plt.boxplot(wine_data[column].dropna())  # 绘制箱线图
    plt.title(f"{column} Boxplot")  # 设置标题

plt.tight_layout()  # 调整子图间距
plt.show()  # 显示图形

# (2) 绘制直方图
plt.figure(figsize=(20, 15))  # 设置图形大小
for i, column in enumerate(wine_data.columns[:-1]):
    plt.subplot(3, 4, i + 1)  # 创建子图
    plt.hist(wine_data[column].dropna(), bins=15)  # 绘制直方图
    plt.title(f"{column} Histogram")  # 设置标题

plt.tight_layout()  # 调整子图间距
plt.show()  # 显示图形

# (3) 绘制累计曲线图
fig, ax = plt.subplots(figsize=(10, 6))
for column in wine_data.columns[:-1]:
    ax.plot(np.cumsum(wine_data[column].dropna()), label=column)  # 绘制累计曲线

ax.set_title('Cumulative Sum of Features')  # 设置标题
ax.legend(loc='upper left')  # 显示图例
plt.show()  # 显示图形

# (4) 绘制字段相关性的热力图
corr_matrix = wine_data.corr()
plt.figure(figsize=(12, 8))
plt.imshow(corr_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(np.arange(len(corr_matrix)), corr_matrix.columns, rotation=90)
plt.yticks(np.arange(len(corr_matrix)), corr_matrix.columns)
plt.title('Correlation Heatmap')
plt.show()