from pysimplesoap.client import SoapClient, SoapFault

# create a simple consumer
client = SoapClient(
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl",
    soap_ns='soap',
    ns = False)

# call a few remote methods
# r1=str(client.get_value(number=1).resultaat)
# print "Het platform is: ", r1
#
# r2=str(client.get_value(number=2).resultaat)
# print "System default encoding: ", r2
#
# r3=str(client.get_value(number=3).resultaat)
# print "Resultaat number=3 :", int(r3) # r3 is a number!
#
# r4=str(client.get_value(number=4).resultaat)
# print "Het aantal processen: ", r4.rstrip() # This is a multiline: strip the newline from the result!
#
# r5=str(client.get_value(number=5).resultaat)
# print "Count services: ", r5.rstrip()
#
# r6 = str(client.get_value(number=6).resultaat)
# print "CPU Usage: ", r6, "%"
#
# r10=float(client.get_value(number=10).resultaat)
# print "Percentage :", r10
#
# r11=float(client.get_value(number=11).resultaat)
# r11a= r11 / 1024 / 1024 / 1024
# print "Geheugen vrij:",round(r11a,2), " GB"
#
# r12=float(client.get_value(number=12).resultaat)
# r12a= r12 / 1024 / 1024 / 1024
# print "Geheugen  in gebruik:",round(r12a,2), " GB"
#
# r13=float(client.get_value(number=13).resultaat)
# r13a= r13 / 1024 / 1024 / 1024
# print "Geheugen totaal",round(r13a,2), " GB"

r14 = client.get_value(number=14).resultaat
print r14

r15 = client.get_value(number=15).resultaat
print r15