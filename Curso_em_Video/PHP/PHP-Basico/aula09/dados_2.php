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
<!-- -5 Rp
7 e 7 Recu
+7 Ap -->
        <?php
            $n1 = isset( $_GET["n1"]) && ($_GET["n1"] != "") ?  ( $_GET["n1"]): " N1 Nulo. ";
            $n2 = isset( $_GET["n2"]) && ($_GET["n2"] != "") ?  ( $_GET["n2"]): " N2 Nulo.";

                $media = ($n1 + $n2)/2 ;
                if ($media < 5){
                    $des = "Reprovado!!";
                } elseif ($media < 7) {
                    $des = "Recuperação!!";
                } else {
                    $des = "Aprovado!!";
                }

            echo "Vc esta: $des Sua media foi de $media ";
        ?>

        <form action="aula09_2.html" method="get">
            <input type="submit" value="Voltar">
        </form>
        
    </div>
</body>
</html>