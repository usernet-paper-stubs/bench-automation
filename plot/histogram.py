import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from os import listdir
from os.path import isfile, join
import csv
import pandas as pd
import seaborn as sns

# ------- data -------

dataset = np.random.default_rng().uniform(60, 95, (20, 4))
df = pd.DataFrame(dataset, columns=['data1', 'data2', 'data3', 'data4'])
df.head()

vals, names, xs = [], [], []
for i, col in enumerate(df.columns):
    vals.append(df[col].values)
    names.append(col)
    # adds jitter to the data points - can be adjusted
    xs.append(np.random.normal(i + 1, 0.04, df[col].values.shape[0]))

plt.boxplot(vals, labels=names, showmeans=True,
            meanline=True, meanprops=dict(label='Average'), medianprops=dict(label='Median'))
palette = ['r', 'g', 'b', 'y']
for x, val, c in zip(xs, vals, palette):
    plt.scatter(x, val, alpha=0.4, color=c)

##### Set style options here #####
# sns.set_style("whitegrid")  # "white","dark","darkgrid","ticks"
# boxprops = dict(linestyle='-', linewidth=1.5, color='#00145A')
# flierprops = dict(marker='o', markersize=1,
#                   linestyle='none')
# whiskerprops = dict(color='#00145A')
# capprops = dict(color='#00145A')
# medianprops = dict(linewidth=1.5, linestyle='-', color='#01FBEE')

plt.xlabel("Categorical", fontweight='normal', fontsize=14)
plt.ylabel("Numerical", fontweight='normal', fontsize=14)
# sns.despine(bottom=True)  # removes right and top axis lines
plt.axhline(y=65, color='#ff3300', linestyle='--',
            linewidth=1, label='Threshold Value')
plt.legend(bbox_to_anchor=(0.31, 1.06), loc=2, borderaxespad=0.,
           framealpha=1, facecolor='white', frameon=True)


plt.show()
