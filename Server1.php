<!DOCTYPE html>
<html lang="en">
<head>
    <title></title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    <style>
        table, th, td {
        border: 1px solid black;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-inverse">
        <div class="container-fluid">

            <!-- Logo -->
            <div class="navbar-header">
                <a href="Website.html" class="navbar-brand">Management site</a>
            </div>

            <!-- Menu Items -->
            <div>
                <ul class="nav navbar-nav">
                    <li class="active"><a href="#">Home</a></li>
                    <li><a href="Server1.html">Server 1</a></li>
                    <li><a href="Server2.html">Server 2</a></li>
                    <li><a href="Server3.html">Server 3</a></li>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
<?php

echo "<html><body><table border="1">\n\n";
$f = fopen("C:\Users\Ward Bakker\PycharmProjects\Python1\Desktop-Ward.csv", "r");
while (($line = fgetcsv($f)) !== false) {
        echo "<tr>";
        foreach ($line as $cell) {
                echo "<td>" . htmlspecialchars($cell) . "</td>";
        }
        echo "</tr>\n";
}
fclose($f);
echo "\n</table></body></html>";

?>

</body>
</html>