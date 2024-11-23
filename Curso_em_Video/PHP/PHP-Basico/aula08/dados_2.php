<!DOCTYPE html>
<html lang="pt-br">
<head>

    <?php
        $txt = isset($_GET["t"]) && ($_GET["t"] !== "") ? $_GET["t"] : "Texto Generico";
        $tam = isset($_GET["tam"]) && ($_GET["tam"] !== "") ? $_GET["tam"] : "12pt";
        $cor = isset($_GET["cor"]) && ($_GET["cor"] !== "") ? $_GET["cor"] : "#000000";
    ?> 

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>

    <link rel="stylesheet" href="styles.css">

    <style>
        span.texto {
            font-size: <?php echo $tam; ?>;
            color: <?php echo $cor; ?>;
        }
    </style>

</head>
<body>


    <div class="c">
        <?php
            echo "<span class='texto'> $txt </span>";
        ?>

        <form method="get" action="aula08_2.html">
            <input type="submit" value="voltar"/>
        </form>
    </div>
</body>
</html>