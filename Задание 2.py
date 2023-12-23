import numpy as np
arr = np.random.randint(1, 10, 100000)
arr.resize(1000, 100)
arr = (np.where(arr > 7, 1, 0)).mean(axis=1)
res_percent = (list(arr).count(0.2) / 1000) * 100
print(f'{res_percent}%')