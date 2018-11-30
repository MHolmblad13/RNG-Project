import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def tentMap(seed, n=5):

    out = np.array([])
    next_x = seed
    for i in range(1, n):
        this_x = next_x
        if this_x < 0.5:
            next_x = 2 * this_x
        elif this_x >= 0.5:
            next_x = 2 - 2 * this_x
            
        out = np.append(out, next_x)
    return out

data = tentMap(0.231095821, 500000)
#print(data)

#pd.Series(data).hist(bins=50)
plt.hist(data, bins=50, color = "blue")
#sns.distplot(data, bins=50, kde=False, rug=False)
plt.show()