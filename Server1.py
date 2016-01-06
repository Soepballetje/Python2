#!C:\Python27\python.exe
import cgi, cgitb
import csv
print "content-Type: text/html\n"
cgitb.enable()

form = cgi.FieldStorage()

with open('names.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    print(row['first_name'], row['last_name'])

print "<!DOCTYPE html>"
print '<html lang="en">'
print "<head>"
print "<title>Server 1</title>"
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
print '<a href="Server1.py" class="navbar-brand">Server 1</a>'
print '</div>'
print '<div>'
print '<ul class="nav navbar-nav">'
print '<li class="active"><a href="#">Home</a></li>'
print '<li><a href="Server2.py">Server 2</a></li>'
print '<li><a href="Server3.py">Server 3</a></li>'
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