from pysimplesoap.client import SoapClient
import csv
from time import strftime
from lxml import etree
import os


hostlist = []

data = 'host1.xml'
xmldata = etree.parse(data)
host= xmldata.xpath('/groep/host/ip/text()')

# hgfhfghfgh

for i in host:
    print i
    client = SoapClient(
        location = 'http://'+i+':8008/',
        action = 'http://localhost:8008/', # SOAPAction
        namespace = "http://example.com/sample.wsdl",
        soap_ns='soap',
        ns = False)

# call a few remote methods
Lists = [[] for i in range(20)]
try:
    r1 = str(client.get_value(number=1).resultaat)
    print "Het platform is: ", r1
    Lists[0].append(r1)
except:
    print("Agent didn't send platform specifications because:")
try:
    r2 = str(client.get_value(number=2).resultaat)
    print "System default encoding: ", r2
    Lists[1].append(r2)
except:
    print("Agent didn't send encoding specifications because:")
try:
    r3=str(client.get_value(number=3).resultaat)
    print "Resultaat number=3:", int(r3)  # r3 is a number!
    Lists[2].append(r3)
except:
    print("Agent didn't send number because:")
try:
    r4 = str(client.get_value(number=4).resultaat)
    print "Het aantal processen: ", r4.rstrip()  # This is a multiline: strip the newline from the result!
    Lists[3].append(r4)
except:
    print("Agent didn't send number of processes because:")
try:
    r5=str(client.get_value(number=5).resultaat)
    print "Count services: ", r5.rstrip()
    Lists[4].append(r5)
except:
    print("Agent didn't send number of services because:")
try:
    r6 = str(client.get_value(number=6).resultaat)
    print "CPU Usage: ", r6, "%"
    Lists[5].append(r6)
except:
    print("Agent didn't send cpu Usage because:")
try:
    r10 = float(client.get_value(number=10).resultaat)
    print "Percentage:", r10, "%"
    Lists[6].append(r10)
except:
    print("Agent didn't send cpu utilization because:")
try:
    r11 = float(client.get_value(number=11).resultaat) / 1024 / 1024 / 1024
    print "Geheugen vrij:", round(r11,2), "GB"
    Lists[7].append(r11)
except:
    print("Agent didn't free hdd space because:")
try:
    r12 = float(client.get_value(number=12).resultaat) / 1024 / 1024 / 1024
    print "Geheugen in gebruik:", round(r12, 2), "GB"
    Lists[8].append(r12)
except:
    print "Agent didn't occupied space because:"
try:
    r13 = float(client.get_value(number=13).resultaat) / 1024 / 1024 / 1024
    print "Geheugen totaal:", round(r13, 2), " GB"
    Lists[9].append(r13)
except:
    print("Agent didn't total free hdd space because:")

try:
    r14 = client.get_value(number=14).resultaat
    print "First IP in range is: ", r14
    Lists[10].append(r14)
except:
    print("Agent didn't report first ip address because:")
try:
    r15 = float(client.get_value(number=15).resultaat) / 1024 / 1024 / 1024
    print "Totaal vrije ruimte", round(r15, 2), "GB"
    Lists[11].append(r15)
except:
    print("Agent didn't disk usage because:")
try:
    r16 = float(client.get_value(number=16).resultaat) / 60 / 60
    print "De uptime van dit systeem betreft:", round(r16, 2)
    Lists[12].append(r16)
except:
    print "Agent didn't uptime because:"

try:
    r17 = str(client.get_value(number=17).resultaat)
    print "Hostname node is:", r17
    Lists[13].append(r17)
except:
    print "Agent didn't send hostname because:"

Time = strftime("%Y-%m-%d %H:%M:%S"), r17, r1, r2, r3, r4, r5, r6, r10, r11, r12, r13, r14, r15, r16
with open(r17+".csv", 'wb') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(["Time", "Hostname", "Platfrom", "Encoding", "Resultaat", "Processen", "Services", "CPU Usage", "RAM %",
                 "RAM Geheugen Vrij", "RAM gebeugen Usage", "RAM totaal", "IP", "HDD ruimte", "System Uptime"])
    wr.writerow(Time)
