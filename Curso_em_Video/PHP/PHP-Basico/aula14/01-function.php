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
            function soma ($a, $b) {
                $s = $a + $b;
                echo "<p> A soma vale $s </p>";
            }

            soma(3,4);
            soma(8,2);
            $x = 15;
            $y = 5; 
            soma($x, $y);
        ?>
    </div>
</body>
</html>