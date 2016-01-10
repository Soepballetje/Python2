from pysimplesoap.client import SoapClient
import csv
from time import strftime
from lxml import etree
import os
import logging
import matplotlib.pyplot as plt

def uitvragen(client,ServerIP):
    Lists = [[] for i in range(20)]

    r1 = str(client.get_value(number=1).resultaat)              # De resultaten r1 in het agent script wordt uitgevraagd.
    if not r1:
        logging.error("r1 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging.
    else:
        print "Het platform is: ", r1
        Lists[0].append(r1)

    r2 = str(client.get_value(number=2).resultaat)              # De resultaten r2 in het agent script wordt uitgevraagd.
    if not r2:
        logging.error("r2 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging
    else:
        print "System default encoding: ", r2
        Lists[1].append(r2)

    r3=str(client.get_value(number=3).resultaat)                # De resultaten r3 in het agent script wordt uitgevraagd.
    if not r3:
        logging.error("r3 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging
    else:
        print "Resultaat nummer= :", int(r3)  # r3 is a number!
        Lists[2].append(r3)

    r4 = str(client.get_value(number=4).resultaat)              # De resultaten r4 in het agent script wordt uitgevraagd.
    if not r4:
        logging.error("r4 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging
    else:
        print "Het aantal processen: ", r4.rstrip()  # This is a multiline: strip the newline from the result!
        Lists[3].append(r4)

    r5=str(client.get_value(number=5).resultaat)                # De resultaten r5 in het agent script wordt uitgevraagd.
    if not r5:
        logging.error("r5 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging
    else:
        print "Count services: ", r5.rstrip()
        Lists[4].append(r5)

    r6 = str(client.get_value(number=6).resultaat)              # De resultaten r6 in het agent script wordt uitgevraagd.
    if not r6:
        logging.error("r6 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging

    else:
        print "CPU Usage: ", r6, "%"
        Lists[5].append(r6)

    r10 = float(client.get_value(number=10).resultaat)          # De resultaten r10 in het agent script wordt uitgevraagd.
    if not r10:
        logging.error("r10 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging
    else:
        print "Geheugen Percentage:", r10, "%"
        Lists[6].append(r10)

    r11 = float(client.get_value(number=11).resultaat) / 1024 / 1024 / 1024 # De resultaten r11 in het agent script wordt uitgevraagd.
    if not r11:
        logging.error("r11 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging
    else:
        r11a = round(r11, 2)
        print "Geheugen vrij:", round(r11, 2), "GB"
        Lists[7].append(r11a)

    r12 = float(client.get_value(number=12).resultaat) / 1024 / 1024 / 1024 # De resultaten r12 in het agent script wordt uitgevraagd.
    if not r12:
        logging.error("r12 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging
    else:
        r12a = round(r12, 2)
        print "Geheugen in gebruik:", round(r12, 2), "GB"
        Lists[8].append(r12a)

    r13 = float(client.get_value(number=13).resultaat) / 1024 / 1024 / 1024 # De resultaten r13 in het agent script wordt uitgevraagd.
    if not r13:
        logging.error("r13 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging
    else:
        r13a = round(r13, 2)
        print "Geheugen totaal:", round(r13, 2), " GB"
        Lists[9].append(r13a)

    r14 = client.get_value(number=14).resultaat     # De resultaten r14 in het agent script wordt uitgevraagd.
    if not r14:
        logging.error("r14 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging
    else:
        print "First IP in range is: ", r14
        Lists[10].append(r14)

    r15 = float(client.get_value(number=15).resultaat) / 1024 / 1024 / 1024 # De resultaten r15 in het agent script wordt uitgevraagd.
    if not r15:
        logging.error("r15 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging
    else:
        r15a = round(r15, 2)
        print "Totaal vrije ruimte", r15a, "GB"
        Lists[11].append(r15a)

    r16 = float(client.get_value(number=16).resultaat) / 60 / 60    # De resultaten r16 in het agent script wordt uitgevraagd.
    if not 16:
        logging.error("r16 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging
    else:
        r16a = round(r16, 2)
        print "De uptime van dit systeem betreft:", round(r16, 2), "uur"
        Lists[12].append(r16a)

    r17 = str(client.get_value(number=17).resultaat)        # De resultaten r17 in het agent script wordt uitgevraagd.
    if not r17:
        logging.error("r17 heeft geen resultaat kunnen uitvragen het volgende adres:" + ServerIP + strftime(" %Y-%m-%d %H:%M:%S")) #Logging
    else:
        print "Hostname node is:", r17
        Lists[13].append(r17)

    try:
       f = open("C:\\inetpub\\wwwroot\\"+r17+'.csv', 'r')   # Een counter wordt toegevoegd aan de CSV bestanden.
       countrdr = csv.DictReader(f)
       totalrows = 1
       for row in countrdr:
         totalrows += 1
       f.close()
    except:
        pass

    Datum = strftime("%Y-%m-%d")                                        # Datum wordt gedefineerd.
    Time = totalrows, strftime("%H:%M:%S"), Datum, r17, r1, r2, r3, r4, r5, r6, r10, r11a, r12a, r13a, r14, r15a, r16a # alle gegevens  uit de opgevraagde functies worden  toegevoegd aan een variable.
    if not os.path.isfile("C:\\inetpub\\wwwroot\\"+r17+".csv"):         # Hier wordt gechecked of het CSV bestand al bestaat of niet. DIt is op basis van computernaam.
        csvbestand = open("C:\\inetpub\\wwwroot\\"+r17+".csv", 'wb')    # ALs deze niet bestaat wordt deze aagemaakt.
        wr = csv.writer(csvbestand, dialect='excel', lineterminator='\n')
        wr.writerow([ "Count", "Time", "Datum", "Hostname", "Platform", "Encoding", "Resultaat", "Processen", "Services", "CPU Usage", "RAM %",
                     "RAM Geheugen Vrij", "RAM gebeugen Usage", "RAM totaal", "IP", "HDD ruimte", "System Uptime"]) # De headers worden toegevoegd aan het CSV bestand.
        wr.writerow(Time)                                               # Alle informatie uit de opgevraagde funties wordt weggeschreven in het CSV bestand.
    else:
        csvbestand = open("C:\\inetpub\\wwwroot\\"+r17+".csv", 'a')     # Als het bestand al wel bestaat wordt deze uitgebreid door middel van een append functie.
        wr = csv.writer(csvbestand, dialect='excel', lineterminator='\n')
        wr.writerow(Time)                                               # Alle informatie uit de opgevraagde funties wordt weggeschreven in het CSV bestand.

# ----------------------------------------------------------------------------------------------------------------------
    list_Ram1 = []                  # lists die gebruikt worden in de grafieken.
    list_Ram2 = []
    list_Ram3 = []
    gebruik = []

    input_file = csv.DictReader(open("C:\\inetpub\\wwwroot\\"+r17+".csv"))  # Het CSV bestand wordt gelezen.
    for row in input_file:
        list_Ram1.append(float(row["RAM %"]))                               # De uit te lezen kolommen.
        list_Ram2.append(float(row["RAM Geheugen Vrij"]))
        list_Ram3.append(float(row["RAM totaal"]))
        gebruik.append(list_Ram3[-1] - list_Ram2[-1])                       # Rekensom om het gebruik te berekenen.

    plt.figure(1)
    plt.subplot(211)
    plt.plot(list_Ram2, label='Vrij geheugen')                         # De lijn met vrij geheugen
    plt.plot(gebruik, label='In gebruik geheugen')                     # De lijn met geheugen wat in gebruik is
    plt.title('RAM statistics')                                        # Titel
    plt.legend()

    plt.subplot(212)
    plt.plot(list_Ram1, label='Gebruik percentage')                    # De lijn met percentage geheugen gebruik.
    plt.xlabel('Metingsnummer')
    plt.ylabel('Percentage %')
    plt.legend()
    plt.savefig("C:\\inetpub\\wwwroot\\"+r17+"RAM.png")                # De plot wordt opgeslagen als afbeelding. Deze wordt ingeladen op de website.

    list_CPU1 = []
    list_CPU2 = []
    input_CPU = csv.DictReader(open("C:\\inetpub\\wwwroot\\"+r17+".csv"))   # CSV wordt gelezen
    for row in input_CPU:
        list_CPU1.append(float(row["CPU Usage"]))                           # De kolommen die gelezen worden, in dit geval het gebruik percentage.
        list_CPU2.append(float(100 - list_CPU1[-1]))                        # Rekensom om het vrije percentage te verkrijgen.
    plt.clf()                                                               # Het figuur wordt uitgewist uit de plot, dit is van belang anders verschijnt er een loop in het figuur.

    plt.figure(2)                                                           # Nieuw figuur
    plt.subplot(311)
    plt.plot(list_CPU1, label='CPU Gebruik')                              # De lijn CPU gebruik.
    plt.plot(list_CPU2, label='CPU Vrij')                                 # De lijn CPU Vrij.
    plt.xlabel('Metingsnummer')
    plt.ylabel('Percentage %')
    plt.legend()
    plt.savefig("C:\\inetpub\\wwwroot\\"+r17+"CPU.png")                     # wordt opgeslagen als afbeelding. Deze wordt ingeladen op de website.
    plt.clf()
# ----------------------------------------------------------------------------------------------------------------------

logging.basicConfig(filename='Python.log', level=logging.ERROR)           # logging wordt aangemaakt.
# ----------------------------------------------------------------------------------------------------------------------

data = 'host.xml'                                                           # In dit XML bestand bevinden zich de hosts die uitgevraagd worden.
xmldata = etree.parse(data)
host = xmldata.xpath('/groep/host/ip/text()')

# ----------------------------------------------------------------------------------------------------------------------

for i in host:
    hostname = i
    try:                                                                    # Er wordt hier verbinding gemaakt met de server. Voordat dit gedaan wordt,
        reply = os.system("ping -n 1 " + hostname)                          # wordt een ping uitgevoerd om te checken of de host wel beschikbaar is.
        if reply == 0:                                                      # Indien deze niet beschikbaar is wordt naar de else gesprongen en een melding host down gezet in de log.
            client = SoapClient(
                location='http://'+i+':8008/',
                action='http://localhost:8008/',  # SOAPAction
                namespace="http://example.com/sample.wsdl",
                soap_ns='soap',
                ns=False)
            uitvragen(client,i)
        else:
            logging.critical("Host down"+hostname+strftime(" %Y-%m-%d %H:%M:%S"))   # Logging


    except:
        pass


# call a few remote methods




