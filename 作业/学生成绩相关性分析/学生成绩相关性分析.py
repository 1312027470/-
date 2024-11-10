import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# 读取Excel文件
file_path = '作业\学生成绩相关性分析\个人信息数据采集表.xlsx'
data = pd.read_excel(file_path)

# (1) 判断表中是否存在空缺值
print("空缺值统计：")
print(data.isnull().sum())

# 处理空缺值的两种方案
# 方案一：删除包含空缺值的行
data_dropna = data.dropna()

# 方案二：用均值填充数值型空缺值，用众数填充分类型空缺值
data_fillna = data.copy()
for column in data.columns:
    if data[column].dtype == 'object':
        data_fillna.loc[:, column] = data[column].fillna(data[column].mode()[0])
    else:
        data_fillna.loc[:, column] = data[column].fillna(data[column].mean())

# 选择方案二进行处理
data = data_fillna

# (3) 相关性验证
# ① 城市生源学生是否更可能过英语四级？
city_vs_cet4 = pd.crosstab(data['城市or农村'], data['通过四级时间'])
chi2, p, dof, expected = chi2_contingency(city_vs_cet4)
print(f"城市生源学生是否更可能过英语四级：p-value = {p}")

# ② 高等数学成绩越好是否大学英语成绩越差？
math_vs_english = data[['高数1、2平均成绩', '大英1']].copy()
correlation = math_vs_english.corr().iloc[0, 1]
print(f"高等数学成绩越好是否大学英语成绩越差：correlation = {correlation}")

# ⑦ 数学成绩好的同学是否计算机课程成绩也好？
math_vs_computer = data[['高数1、2平均成绩', 'C语言成绩']]
correlation = math_vs_computer.corr().iloc[0, 1]
print(f"数学成绩好的同学是否计算机课程成绩也好：correlation = {correlation}")

# ⑬ 高考英语成绩是否会影响大学英语成绩？
gaokao_english_vs_college_english = data[['高考英语成绩', '大英1']]
correlation = gaokao_english_vs_college_english.corr().iloc[0, 1]
print(f"高考英语成绩是否会影响大学英语成绩：correlation = {correlation}")

