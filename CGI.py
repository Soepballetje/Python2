#!C:\Python27\python.exe
import cgi, cgitb, csv
print "content-Type: text/html\n"
cgitb.enable()

f = open('C:\\Users\\Ward Bakker\\PycharmProjects\\Python1\\DESKTOP-Ward.csv')

print "<!DOCTYPE html>"
print '<html lang="en">'
print "<head>"
print "<title>MANAGEMENT</title>"
print '<meta charset="utf-8">'
print '<meta name="viewport" content="width=device-width, initial-scale=1">'
print '<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">'
print '<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>'
print '<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>'
print '<style>'
print 'table, th, td {'\
      'border: 2px solid black;}'\
      '</style>'
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
print '<table>'
print '<tr>'
print '<th>Time</th>'
print '<th>Hostname</th>'
print '<th>Platfrom</th>'
print '<th>Encoding</th>'
print '<th>Resultaat</th>'
print '<th>Processen</th>'
print '<th>Services</th>'
print '<th>RAM %</th>'
print '<th>RAM Geheugen Vrij</th>'
print '<th>RAM gebeugen Usage</th>'
print '<th>RAM totaal</th>'
print '<th>IP</th>'
print '<th>HDD ruimte</th>'
print '<th>System Uptime</th>'
print '</tr>'
print '<tr>'
print '</table>'
print '</div>'
print '</body>'
print '</html>'
