import datetime
import matplotlib.pyplot as plt

x = [datetime.date(2014, 1, 29), datetime.date(2014, 1, 29), datetime.date(2014, 1, 29)]
y = [2, 4, 1]

fig, ax = plt.subplots()
ax.plot_date(x, y, markerfacecolor='CornflowerBlue', markeredgecolor='white')
fig.autofmt_xdate()
ax.set_xlim([datetime.date(2014, 1, 26), datetime.date(2014, 2, 1)])
ax.set_ylim([0, 5])
plt.show()