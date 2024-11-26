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
            $d = isset($_GET["ds"]) ? $_GET["ds"]:0;
            switch ($d) {
                case 2:
                case 3:
                case 4:
                case 5:
                case 6:
                    echo "Levanta e vai estudar! :)";
                    break;
                case 7:
                case 8:
                    echo "Descanse, gafanhoto";
                    break;
                default:
                    echo "OPC Invalida!";
                    break;
            }
        ?>
        <br><br>
        <a href="javascript:history.go(-1)" class="BTN"> Voltar </a>
    </div>
</body>
</html>