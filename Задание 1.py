import numpy as np
arr = np.random.randint(1, 10, 100)
percent = (arr > 7).mean() * 100
print(f'{percent}%')