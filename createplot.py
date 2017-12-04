import matplotlib.pyplot as plt

import plotly.plotly as py
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylabel('Scores')
ax.set_title('Songs')
y = [362, 397, 473, 623, 284, 319, 525, 675, 497,347]
x = [1,2,3,4,5,6,7,8,9]
width = 1
plt.bar(x, y,color="blue",align='center')
plt.show()

# fig = plt.gcf()
# plot_url = py.plot_mpl(fig, filename='mpl-basic-bar')
