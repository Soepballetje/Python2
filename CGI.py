#!C:\Python27\python.exe
import cgi, cgitb, test
print "content-Type: text/html\n"
cgitb.enable()

form = cgi.FieldStorage()

print "<!DOCTYPE html>"
print '<html lang="en">'
print "<head>"
print "<title>MANAGEMENT</title>"
print '<meta charset="utf-8">'
print '<meta name="viewport" content="width=device-width, initial-scale=1">'
print '<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">'
print '<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>'
print '<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>'
print "</head>"
print "<body>"
print '<nav class="navbar navbar-inverse">'
print '<div class="container-fluid">'
print '<div class="navbar-header">'
print '<a href="Website.html" class="navbar-brand">Management site</a>'
print '</div>'
print '<div>'
print '<ul class="nav navbar-nav">'
print '<li class="active"><a href="#">Home</a></li>'
print '<li><a href="#">About</a></li>'
print '<li><a href="#">Contact</a></li>'
print '<li class="dropdown">'
print '<a href="#" class="dropdown-toggle" data-toggle="dropdown">Servers <span class="caret"></span></a>'
print '<li><a href="Server1.html">Server 1</a></li>'
print '<li><a href="Server2.html">Server 2</a></li>'
print '<ul class="dropdown-menu">'
print '<li><a href="Server3.html">Server 3</a></li>'
print '</ul>'
print '</li>'
print '</ul>'
print '</div>'
print '</div>'
print '</nav>'
print '<div>'
print '<TABLE BORDER="1">'
print '<TR><TD>Time</TD>'
print '<TD>Hostname:</TD>'
print '<TD>Platform:</TD>'
print '<TD>Encoding:</TD>'
print '<TD>Resultaat:</TD>'
print '<TD>Processen:</TD>'
print '<TD>Services:</TD>'
print '<TD>CPU Usage:</TD>'
print '<TD>RAM Usage:</TD>'
print '<TD>Vrije RAM:</TD>'
print '<TD>RAM in Gebruik:</TD>'
print '<TD>RAM totaal:</TD>'
print '<TD>IP:</TD>'
print '<TD>HDD ruimte:</TD>'
print '<TD>Sys uptime:</TD></TR>'
print '<TR> <TD>' '</TD></TR>'
print '</TABLE>'

print '</div>'
print '</body>'
print '</html>'
















