import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
data = pd.read_excel(r'resource\车次上车人数统计表.xlsx')
#筛选数据
tb = data.loc[data['车次'] == 'D02',['日期','上车人数']].sort_values('日期')
#设置字体
plt.rcParams['font.sans-serif'] = 'SimHei'  
#构造绘图
x = np.arange(1,len(tb.iloc[:,0])+1)
yl = tb.iloc[:,1]
plt.figure(2)
plt.bar(x,yl)
plt.xlabel('日期')
plt.ylabel('上车人数')
plt.xticks([1,5,10,15,20,24],tb['日期'].values[[0,4,9,14,19,23]],rotation = 45)
plt.title('D02车次上车人数柱状图')

plt.show()