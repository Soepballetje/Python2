from pysimplesoap.client import SoapClient
import csv
from time import strftime
from lxml import etree
import os
import logging

def uitvragen(client,ServerIP):
    Lists = [[] for i in range(20)]

    r1 = str(client.get_value(number=1).resultaat)
    if not r1:
        logging.error("r1 heeft geen resultaat kunnen uitvragen het volgende adres:"+ ServerIP)
    else:
        print "Het platform is: ", r1
        Lists[0].append(r1)


    r2 = str(client.get_value(number=2).resultaat)
    if not r2:
        logging.error("r2 heeft geen resultaat kunnen uitvragen.")
    else:
        print "System default encoding: ", r2
        Lists[1].append(r2)


    r3=str(client.get_value(number=3).resultaat)
    if not r3:
        logging.error("r3 heeft geen resultaat kunnen uitvragen het volgende adres:"+ ServerIP)
    else:
        print "Resultaat nummer= :", int(r3)  # r3 is a number!
        Lists[2].append(r3)


    r4 = str(client.get_value(number=4).resultaat)
    if not r4:
        logging.error("r4 heeft geen resultaat kunnen uitvragen het volgende adres:"+ ServerIP)
    else:
        print "Het aantal processen: ", r4.rstrip()  # This is a multiline: strip the newline from the result!
        Lists[3].append(r4)

    r5=str(client.get_value(number=5).resultaat)
    if not r5:
        logging.error("r5 heeft geen resultaat kunnen uitvragen het volgende adres:"+ ServerIP)
    else:
        print "Count services: ", r5.rstrip()
        Lists[4].append(r5)

    r6 = str(client.get_value(number=6).resultaat)
    if not r6:
        logging.error("r6 heeft geen resultaat kunnen uitvragen het volgende adres:"+ ServerIP)

    else:
        print "CPU Usage: ", r6, "%"
        Lists[5].append(r6)


    r10 = float(client.get_value(number=10).resultaat)
    if not r10:
        logging.error("r10 heeft geen resultaat kunnen uitvragen het volgende adres:"+ ServerIP)
    else:
        print "Percentage:", r10, "%"
        Lists[6].append(r10)

    r11 = float(client.get_value(number=11).resultaat) / 1024 / 1024 / 1024
    if not r11:
        logging.error("r11 heeft geen resultaat kunnen uitvragen het volgende adres:"+ ServerIP)
    else:
        print "Geheugen vrij:", round(r11,2), "GB"
        Lists[7].append(r11)



    r12 = float(client.get_value(number=12).resultaat) / 1024 / 1024 / 1024
    if not r12:
        logging.error("r12 heeft geen resultaat kunnen uitvragen het volgende adres:"+ ServerIP)
    else:
        print "Geheugen in gebruik:", round(r12, 2), "GB"
        Lists[8].append(r12)


    r13 = float(client.get_value(number=13).resultaat) / 1024 / 1024 / 1024
    if not r13:
        logging.error("r13 heeft geen resultaat kunnen uitvragen het volgende adres:"+ ServerIP)
    else:
        print "Geheugen totaal:", round(r13, 2), " GB"
        Lists[9].append(r13)



    r14 = client.get_value(number=14).resultaat
    if not r14:
        logging.error("r14 heeft geen resultaat kunnen uitvragen het volgende adres:"+ ServerIP)
    else:
        print "First IP in range is: ", r14
        Lists[10].append(r14)


    r15 = float(client.get_value(number=15).resultaat) / 1024 / 1024 / 1024
    if not r15:
        logging.error("r15 heeft geen resultaat kunnen uitvragen het volgende adres:"+ ServerIP)
    else:
        print "Totaal vrije ruimte", round(r15, 2), "GB"
        Lists[11].append(r15)



    r16 = float(client.get_value(number=16).resultaat) / 60 / 60
    if not 16:
        logging.error("r16 heeft geen resultaat kunnen uitvragen het volgende adres:"+ ServerIP)
    else:
        print "De uptime van dit systeem betreft:", round(r16, 2)
        Lists[12].append(r16)



    r17 = str(client.get_value(number=17).resultaat)
    if not r17:
        logging.error("r17 heeft geen resultaat kunnen uitvragen het volgende adres:"+ ServerIP)
    else:
        print "Hostname node is:", r17
        Lists[13].append(r17)


    Time = strftime("%Y-%m-%d %H:%M:%S"), r17, r1, r2, r3, r4, r5, r6, r10, r11, r12, r13, r14, r15, r16
    if not os.path.isfile("C:\\Python\\Python2\\"+r17+".csv"):
        kaas = open(r17+".csv", 'wb')
        wr = csv.writer(kaas, dialect='excel', lineterminator ='\n')
        wr.writerow(["Time", "Hostname", "Platfrom", "Encoding", "Resultaat", "Processen", "Services", "CPU Usage", "RAM %",
                     "RAM Geheugen Vrij", "RAM gebeugen Usage", "RAM totaal", "IP", "HDD ruimte", "System Uptime"])
        wr.writerow(Time)
    else:
        kaas = open(r17+".csv", 'a')
        wr = csv.writer(kaas, dialect='excel', lineterminator ='\n')
        wr.writerow(Time)




logging.basicConfig(filename = 'Python.log', level = logging.ERROR)

data = 'host1.xml'
xmldata = etree.parse(data)
host= xmldata.xpath('/groep/host/ip/text()')



for i in host:
    hostname = i
    try:
        reply = os.system("ping -n 1 " + hostname)
        if reply == 0:
            client = SoapClient(
                location = 'http://'+i+':8008/',
                action = 'http://localhost:8008/', # SOAPAction
                namespace = "http://example.com/sample.wsdl",
                soap_ns='soap',
                ns = False)
            uitvragen(client,i)
        else:
            print "host down"


    except:
        pass


# call a few remote methods


