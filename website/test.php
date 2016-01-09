<!DOCTYPE html>
<html lang="en">
<head>
  <title></title>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="5" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <link rel="stylesheet" type="text/css" href="opmaak.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
	<style>
        table, th, td {
        border: 1px solid black;
		padding: 5px;
		border-collapse: collapse;
        }
    </style>
</head>
<body>

<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar">Server 1</span>
        <span class="icon-bar">Server 2</span>
        <span class="icon-bar">Server 3</span>                        
      </button>
      <a class="navbar-brand" href="#">Management site</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">Home</a></li>
        <li><a href="Server1.html">Server 1</a></li>
        <li><a href="Server2.html">Server 2</a></li>
        <li><a href="Server3.html">Server 3</a></li>
      </ul>
    </div>
  </div>
</nav>

<?php
exec("C:\Python27\python.exe management.py");

echo "<html><body><table border=1px>\n\n";
$f = fopen("C:\Users\Ward Bakker\PycharmProjects\Python1\Desktop-Ward.csv", "r");
while (($line = fgetcsv($f)) !== false) {
        echo "<tr>";
        foreach ($line as $cell) {
                echo "<td>" . htmlspecialchars($cell) . "</td>";
        }
        echo "</tr>\n";
}
fclose($f);

?>
<div id="row1">
	<img class="img-responsive" src="ram.png" width="480" height="480">
</div>  
<div id="row2">
	<img class="img-responsive" src="ram.png" width="480" height="480">
</div>

</body>
</html>
