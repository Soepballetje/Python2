import csv
import matplotlib.pyplot as plt
import datetime.strptime

list_Ram1 = []
list_Ram2 = []
list_Ram3 = []
Time = []
input_file = csv.DictReader(open("Desktop-Ward.csv"))
for row in input_file:
    Time.append(str(row["Time"]))
    list_Ram1.append(float(row["RAM %"]))
    list_Ram2.append(float(row["RAM Geheugen Vrij"]))
    list_Ram3.append(float(row["RAM totaal"]))

print list_Ram1
print list_Ram2
print list_Ram3
print Time

plt.plot(list_Ram1, label='Ram percentage', a)
plt.plot(list_Ram2, label='Vrije Ram geheugen')
plt.plot(list_Ram3, label='Totale Ram geheugen')
plt.xlabel('Tijd')
plt.ylabel('Hoeveelheid')
plt.title('Ram statistics')
dates = plt.dates.date2num(Time)
plot_date(dates, values)

plt.legend()
plt.show()
plt.savefig()
