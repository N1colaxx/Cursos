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
            if (!empty($_GET)) {
                for ($i = 1; $i <= 5; $i++) {
                    $v = $_GET["v$i"];
                    echo " Valor $i: $v <br/>";
                };
            } else {
                echo "Nenhum dado foi encontrado!";
            };
        ?>
        <br/>
        
        <a href="javascript:history.go(-1)" class="BTN"> Voltar </a>

    </div>
</body>
</html>