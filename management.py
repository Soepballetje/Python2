from pysimplesoap.client import SoapClient, SoapFault

# create a simple consumer
client = SoapClient(
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    namespace = "http://example.com/sample.wsdl",
    soap_ns='soap',
    ns = False)

# call a few remote methods
r1=str(client.get_value(number=1).resultaat)
print "Het platform is: ", r1

r2=str(client.get_value(number=2).resultaat)
print "System default encoding: ", r2

r3=str(client.get_value(number=3).resultaat)
print "Resultaat number=3 :", int(r3) # r3 is a number!

r4=str(client.get_value(number=4).resultaat)
print "Het aantal processen: ", r4.rstrip() # This is a multiline: strip the newline from the result!

r5=str(client.get_value(number=5).resultaat)
print "Count services: ", r5.rstrip()

r6 = str(client.get_value(number=6).resultaat)
print "CPU Usage: ", r6, "%"