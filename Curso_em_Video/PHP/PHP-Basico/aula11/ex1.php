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
           $c = 1;
           while ($c <= 10) {
            echo $c . "<br/>";
            $c ++;
           }
        ?>

        <?php
            echo "<br/><br/>";
           $c = 10;
           while ($c >= 1) {
            echo $c . "<br/>";
            $c --;
           }
        ?>

<?php
            echo "<br/><br/>";
           $c = 10;
           while ($c >= 0) {
            echo $c . "<br/>";
            $c -= 2;
           }
        ?>

    </div>
</body>
</html>
