import csv
import matplotlib.pyplot as plt


list_Ram1 = []
list_Ram2 = []
list_Ram3 = []
gebruik = []
Time = []
a = [len(Time)]

input_file = csv.DictReader(open("Desktop-Ward.csv"))
for row in input_file:
    Time.append(str(row["Time"]))
    list_Ram1.append(float(row["RAM %"]))
    list_Ram2.append(float(row["RAM Geheugen Vrij"]))
    list_Ram3.append(float(row["RAM totaal"]))
    gebruik.append(list_Ram3[-1] - list_Ram2[-1])

print list_Ram1
print list_Ram2
print list_Ram3

plt.figure(1)
plt.subplot(211)
plt.plot(list_Ram2, label='Vrije Ram geheugen')
plt.plot(gebruik, label='Totale Ram geheugen')
plt.title('Ram statistics')
plt.legend()

plt.subplot(212)
plt.plot(list_Ram1, label='Ram percentage')
plt.xlabel('Tijd')
plt.ylabel('Percentage %')

plt.legend()

plt.savefig('ram.png')
plt.show()
