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
            $n = isset($_GET["num"]) ? $_GET["num"]:0;
            $o = isset($_GET["oper"]) ? $_GET["oper"]:1;

            switch ($o) {
                case 1: 
                    $r = $n * 2;
                    break;
                case 2:
                    $r = $n ^ 3;
                    break;
                case 3:
                    $r = sqrt($n);
                    break;
            }

            echo "O resultado da operacao solicitada foi <span class='foco'> $r <span/>";
        ?>

        <form action="aula10_0.html" method="get">
            <input type="submit" class="BTN" name="Voltar">
        </form>
    </div>
</body>
</html>