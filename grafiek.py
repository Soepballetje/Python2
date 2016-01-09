import csv
import matplotlib.pyplot as plt

list_Ram1 = []
list_Ram2 = []
list_Ram3 = []
input_file = csv.DictReader(open("Roadrunner.csv"))
for row in input_file:
    Time = float(row["Time"])
    list_Ram1.append(float(row["RAM %"]))
    list_Ram2.append(float(row["RAM Geheugen Vrij"]))
    list_Ram3.append(float(row["RAM totaal"]))

print list_Ram1
print list_Ram2
print list_Ram3

plt.plot(list_Ram1, label='Ram percentage')
plt.plot(list_Ram2, label='Vrije Ram geheugen')
plt.plot(list_Ram3, label='Totale Ram geheugen')
plt.xlabel(str(Time))
plt.ylabel('Hoeveelheid')
plt.title('Ram statistics')
plt.legend()
plt.show()
plt.savefig()
