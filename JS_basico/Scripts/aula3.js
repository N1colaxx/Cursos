document.write('<h1> trabalhando com <br> Objetos </h1>')



// CRIAR objeto

let pessoa = {
    nome    : 'Ederson',
    idade   : 40,
    peso    : 83.5, 
    altura  :1.75,
    doador  :false
};

let produtos = {
    descrição   : [],
    preco       : []
};

const carros = {
    marca   : ['Ford', 'fiat', 'GM'],
    modelo  : ['KA', 'Uno', 'Corsa'],
    ano     : [1999, 2005, 2010]
};


// ACESSAR uma propriedade no console
// pode usar . ou ['']
/*
    EXEMPLO
    pessoa.nome
    pessoa.idade
    pessoa.peso

    pessoa['nome']
    pessoa['idede']
    pessoa.['peso']
*/



//OPERAÇÔES 

//IMC
let imc = pessoa.peso / (pessoa.altura*pessoa.altura)
    console.log(imc);

    //.toFixed
    //limita o N° de casas decimais 
    console.log(`IMC: ${imc.toFixed(2)}`);



// ALTERAR/ATUALIZAR valor de uma propriedade
pessoa.nome = 'Edson Main';
produtos.descrição = ['Arroz'];
produtos.preco = [15.50];

//Usando spreed oparator

produtos.descrição = [
    ...produtos.descrição, 'Trigo', 'Carne', 'Mandioca'
];
produtos.preco = [
    ...produtos.preco,5 ,20.50, 18.5
];

//usando o oparator em costant 
carros.marca =  [...carros.marca, 'WV'];
carros.modelo = [...carros.modelo, 'Fusca'];
carros.ano =    [...carros.ano, 1979];