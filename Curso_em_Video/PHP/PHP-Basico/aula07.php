<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

<!-- OP Relacionais  -->
<!-- 
    Maior   $a > $b
    Menor   $a < $b
    Ma ou I $a >= $b
    Me ou I $a <= $b   
    Dife    $a <> $b  or  $a != $b
    igual   $a == $b
    ident   $a === $b
-->

<!-- OP Tenario -->
 <!--
    Usa para comparações SIMPLES.
    
    sintaxe =>  expressão ? verdadeiro=1 : falso=2      O (?) é um comparador
                expre = True , não é, executa false 
    ISSO:
        $maior = $a>$b ? $a:$b   
    É IGUAL A ISSO:
        Se (A > B) entaõ
            maior <- A
        Senao
            maior <- B
        FimSe
 -->

<!-- OP Logicos -->
<!-- 
    E   => and  ou &&
    OU  => or   ou ||    
    XOU => xor
    NÂO => !

-->

    <div class="c">

        <?php
            echo "<br>Hello World, starting in PHP<br><br>";
        ?>

    <!-- ex 1 de OP Tenario -->
        <?php
            // $n1 = $_GET["a"];
            // $n2 = $_GET["b"];
            // $tipo = $_GET["op"];
            
            // echo "Os valores passado foram $n1 e $n2 <br>";
            // $r = ($tipo == "s") ? $n1+$n2 : $n1*$n2;
            // echo "O res será = $r";
        ?>

    <!-- ex 2 de OP Tenario -->
        <?php
            // $a = 3;
            // $b ="3";

            // $r = ($a == $b) ? "sim" : "nao";
            // echo "As var A e B são iguais? $r <br/>";

            // $r = ($a === $b) ? "sim" : "nao";
            // echo "As var A e B são identicas? $r";
        ?>
    

    <!-- ex 3 de Op Tenario -->
     <?php
        // $n1 = $_GET["n1"];
        // $n2 = $_GET["n2"];
        // $m = ($n1 + $n2)/2;
        // echo "A media de N1 e N2 é = $m <br/>";
        // echo "De acordo com a sua media vc " . ($passou = ($m >= 7) ? "está Aprovado!!" : "está Reoprovado!!!");
     ?>

     <!-- ex de OP Logiocs -->
      <?php
        $ano = $_GET["an"];
        $idade = 2024 - $ano;
        echo "Quem nasceu em $ano tem $idade anos,";

        $tipo = ($idade>=18 && $idade<65) ? "OBRIGATORIO" : "NÃO OBRIGATORIO.";
        echo " e dessa forma seu voto é  $tipo";
      ?>

</div>
</body>
</html>