<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <link rel="stylesheet" href="styles.css">
</head>

<!-- 
    usar o ponto ( . ) é uma forma de concatenação em PHP ex: echo "O valor absolurto de $v2 e " . abs($v2);

    Aqui escrevo os valores pela URL ex: localhost/aula05/operadores.php?a=3&b=2
    $n1 = isset ( $_GET["a"]) ? $_GET["a"] : 0;   verifica se a chave a foi definida na URL. Se existir, atribui o valor passado; caso contrário, usa um valor padrão, como 0. 
    condição ? valor_se_verdadeiro : valor_se_falso;

        Funções padrões do PHP 
    |-----------------------------|
    abs()            valor absoluto 
    pow()            Potenciação
    sqrt()           Raiz
    round()          Arredonda, tbm tem => ceil e floor, ceil = para cima / floor = para baixo 
    intval()         parte Interira 
    number_format()  Formatação de N°
-->


<body>
    <div class="c">

        <?php
            echo "<br>Hello World, starting in PHP<br><br>"
        ?>

        <?php 
            // $idade = 18;
            // $nome = "Nicolas";
            
            // echo $nome. " tem ".  $idade. " anos!";

            // echo "<br> <br> ";
            // echo "$nome tem $idade anos !!";
            
            // echo "<br> <br> ";
            // echo '$nome tem $idade anos ';

            // echo "<br><br>";
            
            // // $n1 = 2;
            // // $n2 = 5;

            // $n1 = isset ( $_GET["a"]) ? $_GET["a"] : 0;
            // $n2 = isset ( $_GET["b"]) ? $_GET["b"] : 0;
            // echo "<h2> Valores recebidos: $n1 e $n2 </h2>";


            // $soma = $n1 + $n2;
            // $sub = $n1 - $n2; // Corrigido: n2 - n1
            // $mult = $n1 * $n2;
            // $div = $n1 / $n2;
            // $modulo = $n1 % $n2;
            // $media = ($n1 + $n2) / 2;

            // echo "<br><br>";
            
            // echo "Soma: $soma<br>";
            // echo "Subtração: $sub<br>";
            // echo "Multiplicação: $mult<br>";
            // echo "Divisão: $div<br>";
            // echo "Módulo: $modulo<br>";
            // echo "Média: $media<br>";

            // echo "<br><br>";
        ?>

        <?php 
            $v1 = isset ($_GET["x"]) ? $_GET["x"] : 0;
            $v2 = isset ($_GET["y"]) ? $_GET["y"] : 0;

            echo "<h2> Valores recebidos: $v1 e $v2 </h2>";
            echo "<br/>O valor absolurto de $v2 e " . abs($v2);
            echo "<br/>O valor de $v1<sup> $v2</sup>   e " . pow($v1, $v2);
            echo "<br/>A raiz de $v1 e " . sqrt($v1);
            echo "<br/>O valor de $v2 arredondado e "  . round($v2); // 
            echo "<br/>A parte inteira de $v2 e " . intval($v2);
            echo "<br/>O valor de $v1 em moeda e " . number_format($v1,2,",", ".");
        ?>
    </div>
</body>
</html>
