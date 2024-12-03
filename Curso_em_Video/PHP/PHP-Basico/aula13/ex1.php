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
            for ($i = 1; $i <= 10; $i ++) {
                echo "$i ";
            };
            echo "<br/> <br/>";

            for ($i = 10; $i >= 1; $i --) {
                echo "$i ";
            };
            echo "<br/> <br/>";

            for ($i = 0; $i <= 50; $i +=5) {
                echo "$i ";
            };
            echo "<br/> <br/>";

            for ($i = 30; $i >= 0; $i -=2) {
                print "$i ";
            };
        ?>

    </div>
</body>
</html>