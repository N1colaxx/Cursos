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
            $a = isset($_GET["ano"]) && ($_GET["ano"] != "") ? $_GET["ano"]:1900;
            $i = date("Y") - $a;
            echo "VC nasceu em $a e terá $i anos de idade. <br/>"; 

            If ($i >= 18) {
                $v = " pode Votar";
                $d = " pode Dirigir";
            } else {
                $v = "Não pode Votar";
                $d = "Não pode Dirigir";
            };
            echo "Com essa idade vc $v e tambem $d";
        ?>

        <form method="get" action="aula09.html">
            <input type="submit" value="voltar"/>
        </form>
    </div>
</body>
</html>