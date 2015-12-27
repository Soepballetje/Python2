import matplotlib.pyplot as plt
import numpy as np
import csv

filename = open('DESKTOP-Ward.csv', 'rb')
mycsv = csv.reader(filename)
mycsv = list(mycsv)

time = mycsv[0][0]
hostname = mycsv[1][1]
Platfrom = mycsv[0][2]
encoding = mycsv[0][3]
resultaat = mycsv[0][4]
Processen = mycsv[0][5]
services = mycsv[0][6]
CPU_Usage = mycsv[0][7]
RAM_P = mycsv[0][8]
RAM_Geheugen_Vrij = mycsv[0][9]
RAM_gebeugen_Usage = mycsv[0][10]
RAM_totaal = mycsv[0][11]
IP = mycsv[0][12]
System_Uptime = mycsv[0][13]
print hostname

# fig = plt.figure()
# fig.subplots_adjust(top=0.8)
# ax1 = fig.add_subplot(211)
# ax1.set_ylabel('volts')
# ax1.set_title('a sine wave')
#
# t = np.arange(0.0, 1.0, 0.01)
# s = np.sin(2*np.pi*t)
# line, = ax1.plot(t, s, color='blue', lw=2)
#
# ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
# n, bins, patches = ax2.hist(np.random.randn(1000), 50,
#     facecolor='yellow', edgecolor='yellow')
# ax2.set_xlabel('time (s)')
# fig.savefig('foo.png', dpi=200)