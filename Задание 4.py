import numpy as np
a = np.arange(1, 11)
arr = np.array([a] * 10)
arr_vert_sum = arr.sum(axis=0)
print(arr_vert_sum)