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
        // isset verifica se uma variável foi declarada e não é nula
            $nome = isset($_GET["nome"]) ? $_GET["nome"] : null;
            $ano_nas = isset($_GET["anoNas"]) ? $_GET["anoNas"] : null;
            $sexo = isset($_GET["sexo"]) ? $_GET["sexo"] : null;

            if ($nome === "" or $ano_nas == "" or $sexo == "") {
                echo "Algum campo não foi preenchido!! Volte e Preencha.";
            } else {
                $idade = date("Y") - $ano_nas ;
                echo "$nome tem $idade anos de idade e é $sexo.";
            };
        ?>

        <form method="get" action="aula08_1.html">
            <input type="submit" value="voltar"/>
        </form>
    </div>
</body>
</html>