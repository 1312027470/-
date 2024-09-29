import numpy as np  # type: ignore
import matplotlib.pyplot as plt # type: ignore

x = np.array([1,2,3,4,5,6,7,8])     #横坐标（季度标号）
y = np.array([100,104,106,95,103,105,115,100])  #纵坐标（销售额）
v = ['2018年一季度','2018年第二季度','2018年第三季度','2018年第四季度','2019年第一季度','2019年第二季度','2019年第三季度','2019年第四季度']

plt.rcParams['font.sans-serif'] = 'SimHei'  #设置字体
plt.title('某产品2018-2019各季度销售额')
plt.plot(x,y)
plt.xlabel('季度')
plt.xticks(x,v,rotation = 45)
plt.ylabel('销售额(万元)')

# 显示图像
plt.show()
