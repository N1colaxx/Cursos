<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>
    <link rel="stylesheet" href="styles.css">
</head>


<!-- OP de Atribuição       -->
<!-- 
    adiç    $a = $a + $b    or  $a += $b
    Subi    $a = $a - $b    or  $a -= $b
    Mult    $a = $a * $b    or  $a *= $b
    Divi    $a = $a / $b    or  $a /= $b
    Modu    $a = $a % $b    or  $a %= $b    
    Conc    $a = $a . $b    or  $a .= $b
-->

<!-- OP de Incremento       -->
<!--
    Pré-incre    $a = $a + 1    or  ++$a 
    Pós-incre    $a = $a + 1    or  $a++ 
    Pré-incre    $a = $a - 1    or  --$a 
    Pós-decre    $a = $a - 1    or  $a-- 
-->

<!-- Variaveis referencia   -->
<!-- 
    a var é => &
    $b = &$a;  Aqui to falando q B esta ligado ao A, então sempre B e A tem o mesmo valor.
-->

<!-- Variaveis de Variaveis -->
 <!-- 
    a var é => $$var

    A qui voucrio 2 var: 
        $site = "xxx";
        $$site = "yyy";
    Q fica assim:
        $site q recebe = xxx
    AI cria outra var, que chama:
        $xxx q recebe = yyy
 -->

<body>
    <div class="c">

        <?php
            echo "<br>Hello World, starting in PHP<br><br>";
        ?>

        <!-- OP de Atribuiçaõ -->
        <?php
            // $preco = $_GET["p"];
            // echo " O preço do produto e $preco";
            
            // $preco += ($preco*10/100);
            // echo "<br/> O novo preco com 10% de aumento e $ " . number_format($preco, 2);

            // $preco -= ($preco*10/100);
            // echo "<br/> O novo preco com 10% de desconto e $ " . number_format($preco, 2);
        ?>

        <!-- OP de Incremento -->
        <?php
            // $atual = $_GET["aa"];
            // echo "O ano atual e $atual e o ano anterio e " . --$atual;
        ?>

        <!-- Variaveis referencia  -->
        <?php
            // $a = 3;
            // $b = $a;
            // $b += 5;
            // echo $a . " <--> " . $b;

            // echo "<br/><br/>";

            // $a = 3;
            // $b = &$a;
            // $b += 5;
            // echo $a . " <--> " . $b;
        ?>

        <!-- Variaveis de Variaveis -->
        <?php
            // $x = "abc";
            // $$x = "def";
            // echo " O conteudo da var X é = $x";
            // echo "<br/> A var ABC criada recebeu o valor = $abc";
        ?>

    </div>
</body>
</html>