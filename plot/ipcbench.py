import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from os import listdir
from os.path import isfile, join
import csv
import matplotlib.ticker as ticker
import sys

# ----------- params -----------

if len(sys.argv) < 2:
    print(f"./{sys.argv[0]} [target csv file]")
    exit()

# ----------- data ------------

# ----- throughput -----
data = csv.reader(open(sys.argv[1], newline=''), delimiter=',')

# column_names = data.dialect
header = next(data)[1:]
header_sz = len(header)
# header_color = ['red', 'green', 'yellow',
#                 'black', 'silver', 'blue', 'pink', 'black']
header_color = ['#cc72ff', '#7c97ff', '#808080',
                '#d4d4d4', '#00a5e0', '#fea07b', '#ffd9c2', '#41ab30']

rdma07 = list(map(lambda x: 0 if x == '' else float(x), next(data)[1:]))
intel = list(map(lambda x: 0 if x == '' else float(x), next(data)[1:]))
amd = list(map(lambda x: 0 if x == '' else float(x), next(data)[1:]))
rdma09 = list(map(lambda x: 0 if x == '' else float(x), next(data)[1:]))

columns = []
for i in range(0, len(header)):
    columns.append([header[i], rdma07[i], rdma09[i], intel[i], amd[i]])

# ----- msgrate -----
mdata = csv.reader(open('ipcbench.msgrate.csv', newline=''), delimiter=',')

next(mdata)
mrdma07 = list(map(lambda x: 0 if x == '' else float(x), next(mdata)[1:]))
mintel = list(map(lambda x: 0 if x == '' else float(x), next(mdata)[1:]))
mamd = list(map(lambda x: 0 if x == '' else float(x), next(mdata)[1:]))
mrdma09 = list(map(lambda x: 0 if x == '' else float(x), next(mdata)[1:]))

mcolumns = []

mcolumns.append([header[0], mrdma07])
mcolumns.append([header[1], mrdma09])
mcolumns.append([header[2], mintel])
mcolumns.append([header[3], mamd])


# ----------- plot ------------

# ----- styles -----

csfont = {'fontname': 'CMU Serif'}
plt.rcParams["font.family"] = "CMU Serif"
axis_label_font_size = 18
axis_ticks_font_size = 18
legend_font_size = 10

# ----- data -----

fig, ax = plt.subplots()
ax2 = ax.twinx()

# plt.xticks(x, header)
# plt.tick_params(
#     axis='x',
#     which='both',
#     bottom=False,
#     top=False,
#     labelbottom=False)
# plt.xlabel('rdma07')
# plt.bar(x, rdma07, color=header_color)
# ax.bar(x - 0.35/2, )


x = np.arange(4)
width = 1.0
i = 0
for c in columns:
    bar = ax.bar(x - (width/len(columns)*(i - len(columns)/2+1)),
                 c[1:], width/len(columns)-0.01, label=c[0], edgecolor='black')
    # ax.bar_label(bar, '', padding=3)
    # print(mcolumns[i][1:])
    # print([x[i] - (width/len(columns)*(0 - len(columns)/2+1)), x[i] -
    #        (width/len(columns)*(1 - len(columns)/2+1)), x[i] -
    #        (width/len(columns)*(2 - len(columns)/2+1)), x[i] -
    #        (width/len(columns)*(3 - len(columns)/2+1))])

    i += 1

i = 0
for c in mcolumns:
    pos_x = []

    for d in range(len(c[1])):
        pos_x.append(x[i] - (width/len(columns)*(d - len(columns)/2+1)))

    ax2.plot(
        # [x - width / 2, x + width / 2],
        pos_x,
        c[1],
        color='black', marker='x', mec='k'
    )

    i += 1

ax.set_xticks(x, ['rdma07', 'rdma09', 'intel', 'amd'],
              fontsize=axis_ticks_font_size)
plt.setp(ax.get_yticklabels(), fontsize=axis_ticks_font_size)


# colors = {'fruit': 'red', 'veggie': 'green'}
# colors = dict(zip(header, header_color))
# labels = list(colors.keys())
# handles = [plt.Rectangle((0, 0), 1, 1, color=colors[label])
#            for label in labels]
# plt.legend(handles, labels)

# ----- legend ----

ax.legend(ncol=int(len(columns)/2), fontsize=legend_font_size)

fig.tight_layout()

# ----- axis -----

ax.set_axisbelow(True)
ax.grid(axis='both', color='0.95')
for axis in ['top', 'bottom', 'left', 'right']:
    ax.spines[axis].set_linewidth(2.0)
ax.set_ylabel("Throughtput (us)", **csfont, fontsize=axis_label_font_size)


# ax2.yaxis.set_major_formatter(
#     ticker.FuncFormatter(lambda y, _: '{:g}'.format(y)))
# ax2.yaxis.set_major_formatter(
#     ticker.FuncFormatter(lambda y, _: y))

ax2.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda y, _: '{:2.2e}'.format(y)))
# ax2.set_ylabel("$10^x$")
# ax2.set_yscale('log')
ax2.set_ylabel("Message Rate (msg/s)", **csfont, fontsize=axis_label_font_size)

# ----- style ----

plt.show()
