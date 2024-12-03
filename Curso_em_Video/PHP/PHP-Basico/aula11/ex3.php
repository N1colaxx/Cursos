<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>
    <link rel="stylesheet" href="styles.css">
</head>

    <script>
        function validateForm() {
            const ini = document.querySelector('input[name="ini"]').value;
            const fin = document.querySelector('input[name="fin"]').value;
            const inc = document.querySelector('input[name="inc"]').value;

            // Verifica se todos os campos estão preenchidos
            if (!ini) {
                alert("O campo 'Inicio' não foi preenchido! Preencha.");
                return false;
            }
            if (!fin) {
                alert("O campo 'Final' não foi preenchido! Preencha.");
                return false;
            }
            if (!inc) {
                alert("O campo 'Incremento' não foi preenchido! Preencha.");
                return false;
            }

            // Se tudo estiver preenchido, permite o envio
            return true;
        }
    </script>

<body>
    <div class="c">

        <?php
            echo "<br>Hello World, starting in PHP<br><br>";
        ?>
        
        <form action="ex3-0.php" method="get" onsubmit="return validateForm()">
            Inicio: <input type="number" name="ini" min="0" max="500" />
            <br><br>
            Final: <input type="number" name="fin" min="0" max="500" />
            <br><br>
            Incremento: <input type="number" name="inc" min="1" max="10">
            <br><br>

            <input type="submit" value="Enviar" class="BTN" />
        </form>

    </div>
</body>
</html>