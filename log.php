<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="refresh" content="60" />
    <title></title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>

<style>
    table, th, td {
    border: 1px solid black;
    padding: 5px
    }
</style>

</head>
<body>

    <nav class="navbar navbar-inverse">
        <div class="container-fluid">

            <!-- Logo -->
            <div class="navbar-header">
                <a href="CGI.py" class="navbar-brand">Management site</a>
            </div>

            <!-- Menu Items -->
            <div>
                <ul class="nav navbar-nav">
                    <li><a href="CGI.py">Home</a></li>
                    <!-- drop down menu -->
                            <li><a href="Server1.php">Server 1</a></li>
                            <li><a href="Server2.php">Server 2</a></li>
                            <li><a href="Server3.php">Server 3</a></li>
                            <li class="active"><a href="log.php">Server logging</a></li>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</div>
<?php


echo file_get_contents( "Python.log" );
?>
</body>
</html>