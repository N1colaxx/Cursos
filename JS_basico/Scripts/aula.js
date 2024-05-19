



let mensagem = "Minha mensagem";
let mensagem2 = "outra mesagem";
let meuPeso = 83.5;
let minhaAltuta = 1.75;
let minhaIdade = 40;
let ehDoador = false;
let tetes = null;



//  Criar CONSTANTES  e atribuir valor 
//  uma variavel em JS é armasenada na memoria e pode modificar o conteudo dentro dela.

// escrevendo o conteudo de variaveis e constantes 

const PI = 3.1415;
const TAXA = 0.5;


// formas de escrever Conteudo de Variaveis e  Constantes 

// aspas "" ou '' da na mesma pode usar a que vc preferir
document.write("<p> Mensagem " + minhaAltuta + "m, é esta <p>");
document.write('<p> Mensagem ' + minhaAltuta + 'm, é esta <p>');
document.write(`mensagem : ${mensagem2}`);

document.write("<p>Peso: " + meuPeso + "Kg </p>");
document.write(`Peso: ${meuPeso} é esse ai `);


// OPERAÇÕES E OPERADORES

//  sinal de = 1 vez serve pra atribuir um valor ex: 
let n1 = 10;  // N° int
let n2 = 2;  //N° int
let n3 = "2"; // string -> tipo texto
let n4 = "texto";

document.write("<h1> Operações e Operadores </h1>");
document.write(`N1 ${n1} <br>`);
document.write(`N2 ${n2} <br>`);
document.write(`N3 ${n3} <br>`);

console.log(n1 + n2); //adição
console.log(n1 - n2); //subtração
console.log(n2 * n1); //multiplicação
console.log(n1 / n2); //divisão 
console.log(n1 % n2);  // resto ou modulo 

console.log(n2 == n3); //igual a, referente ao conteudo da var
console.log(n2 === n3); //identico a, referente ao conteudo e o tipo dela da var
console.log(n2 != n3); // diferente de , referente ao conteudo da var
console.log(n2 !== n3); // não é identico a, referente ao conteudo e o tipo dela da var


// OPERADORES LOGICOS
document.write('<h1> Operadores logicos </h1> ')

console.log (n1 > n2) //  n1 for maior que n2
console.log(n1 < n2 ) //  n1 for menor que n2
console.log(n1 >= n2 ) // for maior ou igual a n2
console.log(n1 <= n2) // n1 for menor ou igual a n2

let a = true
let b = false

console.log(a && b )  // E AND, ele retorna o PRIMEIRO valor falso encontrado, ou o último valor se todos os valores forem avaliados como verdadeiros.

console.log (a || b)   //ou OR, Ele retorna o OPRIMEIRO valor verdadeiro encontrado, ou o último valor se todos os valores forem avaliados como falsos.

console.log(!a) //NOT, Ele inverte o valor de verdade (true) para falso (false) e vice-versa.
console.log(!b)