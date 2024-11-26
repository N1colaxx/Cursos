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
            $a = isset($_GET["ano"]) && ($_GET["ano"] != "") ? $_GET["ano"]:"Ano não Preenchido, volte e preencha";

            if ($a === $_GET["ano"]) {
                $i = date("Y") - $a;
                echo "VC nasceu em $a e terá $i anos de idade. <br/>"; 
    
                if ($i < 16) {
                    $tV = "não vota.";
                } elseif (($i >= 16 && $i < 18) || ($i > 65)) {
                    $tV = "Voto é opcional.";
                } else {
                    $tV = "Voto é obtigatorio!";
                }
                echo "Com essa idade, $tV ";
                
            } else {
                echo $a;
            }
        ?>

        <form method="get" action="aula09_1.html">
            <input type="submit" value="voltar"/>
        </form>
    </div>
</body>
</html>