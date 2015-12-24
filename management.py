from pysimplesoap.client import SoapClient, SoapFault

# create a simple consumer
client = SoapClient(
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/',  # SOAPAction
    namespace = "http://example.com/sample.wsdl",
    soap_ns='soap',
    ns = False)

# call a few remote methods
try:
    r1=str(client.get_value(number=1).resultaat)
    print "Het platform is: ", r1
except:
    print("Agent didn't send platform specifications because:")

try:
    r2=str(client.get_value(number=2).resultaat)
    print "System default encoding: ", r2
except:
    print("Agent didn't send encoding specifications because:")

try:
    r3=str(client.get_value(number=3).resultaat)
    print "Resultaat number=3:", int(r3) # r3 is a number!
except:
    print("Agent didn't send number because:")

try:
    r4=str(client.get_value(number=4).resultaat)
    print "Het aantal processen: ", r4.rstrip()  # This is a multiline: strip the newline from the result!
except:
    print("Agent didn't send number of processes because:")

try:
    r5=str(client.get_value(number=5).resultaat)
    print "Count services: ", r5.rstrip()
except:
    print("Agent didn't send number of services because:")

try:
    r6 = str(client.get_value(number=6).resultaat)
    print "CPU Usage: ", r6, "%"
except:
    print("Agent didn't send cpu Usage because:")

try:
    r10=float(client.get_value(number=10).resultaat)
    print "Percentage:", r10
except:
    print("Agent didn't send cpu utilization because:")

try:
    r11=float(client.get_value(number=11).resultaat)
    r11a= r11 / 1024 / 1024 / 1024
    print "Geheugen vrij:",round(r11a,2), "GB"
except:
    print("Agent didn't free hdd space because:")

try:
    r12=float(client.get_value(number=12).resultaat)
    r12a= r12 / 1024 / 1024 / 1024
    print "Geheugen in gebruik:",round(r12a,2), "GB"
except:
    print("Agent didn't occupied space because:")

try:
    r13=float(client.get_value(number=13).resultaat)
    r13a= r13 / 1024 / 1024 / 1024
    print "Geheugen totaal:",round(r13a,2), " GB"
except:
    print("Agent didn't total free hdd space because:")

try:
    r14 = client.get_value(number=14).resultaat
    print "First IP in range is: ", r14
except:
    print("Agent didn't report first ip address because:")

try:
    r15 = float(client.get_value(number=15).resultaat)
    r15a = r15 / 1024 / 1024 / 1024
    print "Totaal vrije ruimte",round(r15a,2), "GB"
except:
    print("Agent didn't disk usage because:")
try:
    r16 = float(client.get_value(number=16).resultaat)
    r16a = r16 / 60 / 60
    print "De uptime van dit systeem betreft:",round(r16a,2)
except:
    print("Agent didn't uptime because:")