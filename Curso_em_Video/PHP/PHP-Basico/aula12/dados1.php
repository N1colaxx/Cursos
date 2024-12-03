<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="c">

        <?php
            $v = isset($_GET["tab"]) ? $_GET["tab"] : 0;
            echo "<h1> A tabuada de $v: <br/>";
            
            $c = 0;
            do {
                $tab = $v * $c; 
                echo "$v X $c = $tab <br/>";
                $c ++;
            }  while ($c <= 10);
            
        ?>
        <br>

        <a href="ex3.html" class="btn"> Vlotar </a>

    </div>
</body>
</html>