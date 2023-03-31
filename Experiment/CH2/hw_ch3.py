#1


import pandas as pd
import numpy as np
data = pd.read_csv('c:/data/cars93.csv', index_col = 0)
midsize = data.loc[data.Type == 'Midsize',:]
print(len(midsize)) # Answer = 22
print(np.mean(midsize.Wheelbase).round(3)) # 107.40

usa = data.loc[data.Origin=='USA', : ]
non_usa = data.loc[data.Origin=='non-USA', : ]

np.mean(usa.Price)
np.mean(non_usa.Price)

#3

import numpy as np
np.random.seed(10)
mat = np.random.randint(1, 101, size=(5,10))
mat

mat_24 = mat[1:5, :]
mat_24

mat_7 = mat[:,6]
print(np.mean(mat_7)) # 평균
print(np.var(mat_7)) # 분산



#4

import numpy as np
np.random.seed(30)
arr = np.random.randint(1, 1001, size=100)
arr2 = np.array([])
for i in arr:
    if i%3 == 0:
        arr2 = np.append(arr2, np.array([1]))
    else:
        arr2 = np.append(arr2, np.array([0]))

print(np.mean(arr2))
print(np.std(arr2))