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
            $v = isset($_GET["val"]) ? $_GET["val"] : 1;
            echo "<h1> Calculando o Fatorial de $v ";

            $c = $v;
            $fat = 1;
            do {
                $fat = $fat * $c;
                $c --;
            } while ($c >= 1);

            echo "<h2> $v! = $fat";
        ?> 
        <br>

        <a href="ex2.html" class="btn"> Voltar </a>

    </div>
</body>
</html>