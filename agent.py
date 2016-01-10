"""
Usage:
Portable Python installed in c:\P2.7.6.1 and agent script in c:\scripts\agent.py
Open the firewall if needed and start this agent:
<cmd>
c:\\P2\App\python.exe c:\scripts\agent.py
"""

from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer
import sys, subprocess
import psutil
import socket
from uptime import uptime
# ---------------------------------------------------------


# List of all your agent functions that can be called from within the management script.
# A real developer should do this differently, but this is more easy.
def get_value(number):
    "return the result of one of the pre-define numbers"
    print "get_value, of of item with number=", number

    # An example of a value that is acquired using Python only.
    # returns a string
    if number == 1:
        return sys.platform

    # Another example of a value that is acquired using Python only.
    # returns a string
    if number == 2:
        return sys.getdefaultencoding()

    # Useless of course but returning an int
    if number == 3:
        return 8888

    # Example in which a PowerShell script is used. The STDOUT is used to pass results back to python.
    # Exporting with export-csv and reading the CSV using Python is also possible of course.
    if number == 4:
        p = subprocess.Popen(['powershell.exe',                # Atlijd gelijk of volledig pad naar powershell.exe
            '-ExecutionPolicy', 'bypass',                      # Override current Execution Policy
            "C:\\Python\\agent_counters.ps1"],                 # Naam van en pad naar je PowerShell script
            stdout=subprocess.PIPE)                            # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                               # De stdout
        return output

    # Example of sing a PowerShell oneliner. Useful for simple PowerShell commands.
    if number == 5:
        p = subprocess.Popen(['powershell',
            "get-service | measure-object | select -expandproperty count"],
            stdout=subprocess.PIPE)                       # Zorg ervoor dat je de STDOUT kan opvragen.
        output = p.stdout.read()                          # De stdout
        return output

    if number == 6:                                             # CPU percentage dat in gebruik is wordt opgevraagd.
        return str(psutil.cpu_percent())
    if number == 10:
        return psutil.virtual_memory().percent                  # RAM percentage dat in gebruik is wordt opgevraagd.
    if number == 11:
        return psutil.virtual_memory().free                     # RAM totaal dat vrij is wordt opgevraagd, dit is in bits.
    if number == 12:
        return psutil.virtual_memory().used                     # RAM totaal dat in gebruik is wordt opgevraagd, dit is in bits.
    if number == 13:
        return psutil.virtual_memory().total                    # RAM totaal dat het systeem heeft wordt opgevraagd.
    if number == 14:
        return socket.gethostbyname(socket.gethostname())       # Het eerste IP adres wordt opgevraagd.
    if number == 15:
        z = subprocess.Popen(['powershell.exe',                 # Vrije ruimte op de schijf C wordt opgevraagd doormiddel van powershell.
            "Get-PSDrive C | foreach {$_.free}"],
            stdout=subprocess.PIPE)
        zoutput = z.stdout.read()
        return zoutput
    if number == 16:                                            # De uptime van het systeem wordt opgevraagd.
        return uptime()
    if number == 17:                                            # De hostname van het systeem wordt opgevraagd.
        return socket.gethostname()
    # Last value
    return None

# ---------------------------------------------------------

# do not change anything unless you know what you're doing.
port = 8008
dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/',  # SOAPAction
    namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)

# do not change anything unless you know what you're doing.
dispatcher.register_function('get_value', get_value,
    returns = {'resultaat': str},   # return data type
    args = {'number': int}         # it seems that an argument is mandatory, although not needed as input for this function: therefore a dummy argument is supplied but not used.
    )

# Let this agent listen forever, do not change anything unless needed.
print "Starting server on port",port,"..."
httpd = HTTPServer(("", port), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()

