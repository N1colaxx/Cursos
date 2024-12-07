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
            if ($_SERVER["REQUEST_METHOD"] == "GET") {
                $num = intval($_GET["num"]);
        
                if ($num <= 0) {
                    echo "<p>Por favor, insira um número positivo maior que zero.</p>";
                }
            }
            
            $divisores = [];
            for ($i = 1; $i <= $num; $i ++) {
                if ($num % $i == 0) {
                    $divisores[] = $i;
                };
            };

            $multiplos = [];
            for ($i = 1; $i <= $num; $i ++) {
                if ($i % $num == 0) {
                    $multiplos[] = $i;
                };
            };

            $isPrimo = count($divisores) == 2;

            echo "<p>Múltiplos de $num: " . implode(", ", $multiplos) . "</p>";
            echo "<p>Divisível por: " . implode(", ", $divisores) . "</p>";

            if ($isPrimo) {
                echo "<p>Então $num é primo.</p>";
            } else {
                echo "<p>Então $num não é primo.</p>";
            }
        ?>
        <br><br>

        <a href="javascript:history.go(-1)" class="btn"> Voltar </a>
    </div>
</body>
</html>