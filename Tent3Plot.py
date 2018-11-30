import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def tentMap(seed, n=5):
    out = np.array([])
    nextx = seed
    for i in range(1, n):
        this = nextx
        if this <= 1/3:
            nextx = 3 * this
        elif this <= 2/3:
            nextx = 2 - this * 3
        elif this <= 1:
            nextx = 3 * this - 2

        out = np.append(out, nextx)
    return out

data = tentMap(0.487356234, 300000)
#print(data)

#pd.Series(data).hist(bins=50)
plt.hist(data, bins=50, color="blue")
#sns.distplot(data, bins=50, kde=False, rug=False)
plt.show()