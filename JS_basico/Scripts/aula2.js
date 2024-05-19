
    document.write('<h1> Arrays - Vetor ou Matriz </h1>')


    let produtos = ['Arroz', 'Feijão', 'leite']
    var codigos = Array(10, 20, 30)
    let meses = ['jan', 'fev', 'mar', 'abr']

    var test = Array(10)
    let testi = Array(10)
    // Add um dado ao arrey
    test[0] = "oi"
    test[9] = "Tudo bem?"
    test[10] = 'opa'

    //como ja tinha um DADO neste indece ele auterou o dado existente para o novo
    meses[0] ='Janeiro'


    //  ADICIONAR no final  do array -> push = empurre 
    produtos.push('Açúcar', 'Trigo');
    codigos.push(40, 50, 60, 70);
    meses.push('mai', 'jun', 'ago', '07');

    //  REMOVER do final  do array -> pop = estourar
    produtos.pop()
    codigos.pop()
    meses.pop()

    //  ADD no inicio  do array -> unshift
    produtos.unshift('coca', 'peps')

     //  Remover no inicio  do array -> shift
     produtos.shift('coca')


    //  REMOVER valores de um posição expecifica -> splice
    //posicao inicial, quantos remover
    codigos.splice(1, 1) //primeiro vc escolher o N°de partida ex: 1 e o N° sub sequente é a quantide de N° que serão deletados

    // COPIAR array -> slice = fatiar porção 
    //posicao inicial, quantos copiar
       meses  = meses.slice(); 
   let meses1 = meses.slice(3,7);
   let meses2 = meses.slice(0,3)


    // NO consele do desenvolvedor se vc colocar LENGTH vc iraver o tamanho do seu array.


    //spreed oparetor -> ...
    // sim os 3 pontos é a tag, ele copia o array todo
    let teste = [ ...produtos, 'Ovo', 'Pera']