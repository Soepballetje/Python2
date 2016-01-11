Dit is een Readme om de management Tool te installeren. Ook worden delen individueel uitgelegd. 

Dit programma is geschreven door de studenten Ward Bakker en Tim Lambers van de Hogeschool Utrecht.


Een link naar onze Github:  https://github.com/Soepballetje/Python2/


Installatie.
-----------
Automatisch

-Installeer de agent.exe op de hosts.
-installeer de management.exe op de management server.
------------
Handmatig
------------
Management installatie:
  Om het management script te kunnen installeren zijn er een aantal prerequisites.
    -Windows Server 2012 r2
    -IIS role
    -Python 2.7.9
    -Numpy
    -Matplotlib
    -PySimpleSoap
    -lxml
    -PHP
    
  Installatie
    - Plaats het management.py en het host.xml bestand in de directory C:\python\
    - Plaats de volgende bestanden in de directory C:\inetpub\wwwroot\
                - CGI.py
                - Server1.php
                - Server2.php
                - Server3.php
  
  Om de management informatie stroom continu te behouden dient er een task aangemaakt te worden die iedere minuut dit script uitvoert.   Wij raden aan om het volgende in een batch bestand te plaatsen en dit te laten uitvoeren door een task:
    - start C:\Python27\python.exe C:\Python\management.py
  
  
Agent installatie:
  Om de agents te kunnen laten functioneren zijn er een aantal prerequisites.
  - Python 2.7.9
  - psutil
  - pysimplesoap

  Installatie
    - Plaats het agent.py en agent_counters.ps1 in de directory C:\python\
  
Om ervoor te zorgen dat het script niet inactief wordt na een eventuele restart van het systeem, raden wij aan om ook hiervoor een task aan te maken. Deze task zal het agent.py script moeten uitvoeren zodra de machine is opgestart. 
    




Toelichting indiviuele delen
----------------------------

PySimpleSoap
----------------------------
PySimpleSoap is een library die clients en server met elkaar laat communiceren. Dit maakt ,zoals de naam suggereert, gebruik van SOAP. 
