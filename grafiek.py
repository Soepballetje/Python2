import csv
import matplotlib.pyplot as plt
import numpy

input_file = csv.DictReader(open("DESKTOp-ward.csv"))
for row in input_file:
    print float(row["RAM %"])
    print float(row["RAM Geheugen Vrij"])
    print float(row["RAM totaal"])


RAM_perc = float(row["RAM %"])
RAM_Vrij = float(row["RAM Geheugen Vrij"])
RAM_totaal = float(row["RAM totaal"])
