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
        <form action="ex2-0.php" method="get">
            <?php
            $c = 1;
            while ($c <= 5) {
                echo "Valor $c: <input type='number' name='v$c' max='100' min='0' value='0' required/>";
                echo "<br/>";
                $c++;
            }
            ?>
            <br>
            <input type="submit" value="Enviar" class="BTN" />


        </form>
    </div>
</body>
</html>