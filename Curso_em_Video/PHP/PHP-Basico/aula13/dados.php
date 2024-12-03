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
            echo "<h1> tabuado do $v <br/><br/>";

            for ($i = 0; $i <=10; $i ++){
                $tab = $v * $i;
                print "$v X $i = $tab <br/>";
            }
        ?>

        <a href="ex2.html" class="btn"> Voltar </a>

    </div>
</body>
</html>