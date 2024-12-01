import pandas as pd
import numpy as np
data = pd.read_excel('resource\missing.xlsx')
print(data)
c = np.array([[1, 2, 3,4], [4, 5, 6, np.nan], [5,6,7, 8],[9,4,np.nan,8]])
c = pd.DataFrame(c)