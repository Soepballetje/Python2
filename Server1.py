#!C:\Python27\python.exe
import cgi, cgitb

print "content-Type: text/html\n"
cgitb.enable()

form = cgi.FieldStorage()

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
print '<li class="active"><a href="">Home</a></li>'
print '<li><a href="Server1.py">Server 1</a></li>'
print '<li><a href="Server2.html">Server 2</a></li>'
print '<li><a href="Server3.html">Server 3</a></li>'
print '</ul>'
print '</li>'
print '</ul>'
print '</div>'
print '</div>'
print '</nav>'
print '<div>'
print '</div>'
