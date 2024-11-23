<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Div Expansível com PHP</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="centralizada">

        <?php
            echo "<br>Hello World, starting in PHP<br><br>"
        ?>

        <?php 
            $idade = 18;
            $nome = "Nicolas";
            
            echo $nome. " tem ".  $idade. " anos!";

            echo "<br> <br> ";
            echo "$nome tem $idade anos !!";
            
            echo "<br> <br> ";
            echo '$nome tem $idade anos ';

            
        ?>




    </div>
</body>
</html>
