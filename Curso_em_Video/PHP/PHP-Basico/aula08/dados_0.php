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
            $valor = isset($_GET["v"]) ? $_GET["v"] : null;

            if ($valor === '') {
                echo "Campo vazio! Volte e digite novamente.<br/>";
            } else {
                echo "O valor enviado foi: $valor<br/>";
                $rq = sqrt($valor);
                echo "A raiz quadrada de $valor é: $rq";
            }
        ?>

        <br><br>
        <form method="get" action="aula08.html">
            <input type="submit" value="voltar"/>
        </form>
    </div>
</body>
</html>