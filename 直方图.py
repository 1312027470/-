import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False 
movie =['新蝙蝠侠','狙击手','奇迹笨小孩'] 
real_day1=np.array( [4053, 2548,1543]) 
real_day2=np.array([7840,4013,2421]) 
real_day3=np.array([8080,3673,1342])#确定距离左侧
left_day2=real_day1
left_day3 =real_day1 +real_day2#设置线条高度 
height =0.2#绘制图形
plt.barh(movie, real_day1, height=height)
plt.barh(movie, real_day2, left=left_day2, height=height) 
plt.barh(movie, real_day3, left=left_day3, height=height)#设置数值文本，计算宽度值和y轴位置
sum_data =real_day1 +real_day2+real_day3 
for i in range(len(movie)):
 plt.text(sum_data[i],movie[i],sum_data[i],va="center" , ha="left")
plt.title("各电影票房") 
plt.xlabel("票房(万)") 
plt.ylabel("电影名称") 
plt.show()