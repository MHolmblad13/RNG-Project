import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import pandas as pd
import seaborn as sns

def logMap(seed, n=5):

    out = np.array([])
    nextx = seed
    for i in range(1, n):
        this = nextx
        if this <= 1:
            nextx = (4 * this) * (1 - this)
        out = np.append(out, nextx)
    return out

data = logMap(0.231095821, 5000)

#pd.Series(data).hist(bins=11)
plt.hist(data, bins=50, color = "blue")
#sns.distplot(data, bins=50, kde=False, rug=False, color='#0038A8')
plt.show()
