

# Volumes

### O que são ?

-    Forma pratica de manter dados, pois `não dependem do container`.
-   Geralmete usado para fazer Beckups 

### Tipos ?

Temos 3 tipos:

-   Anônimo (anonymous)
-   Nomeados (named)
-   Bind moutns

#### O problema da persistência.

-   Se criarmos um container com alguma img, todos so arquivos gerados serão do container;
-   Se viermos a remover o container perderemos todos os arquivos;

---

<br>

## `Comandos` 

docker **volumes ls**

    Consegue ver todos os volumes do nosso ambiente.



docker **volume inspect nome**

    Temos acesso ao local onde o volume guarda dados.

    O docker guarda dados em um diretorio do nosso pc assim, sabemos onde é;



docker **volume rm nome**

    Remove o volume 



Docker **volume prune**

    Remove todos os volumes não utilizados.

---



### `Criando Volumes`


#### Criando <u>Anonymus</u>

    docker run -v /data
    
    obs> DATA sera o diretorio que contem o volume anomimo;

    Ex:

    docker run -v /data phpmenssages




### Criando <u>Named</u>

    docker run -v nome_do_volume:/data

    ex: -v php_volue:/var/www/html/menssages



### Criando <u>Bind mouns</u>

    docker run -v /dir/data:data

    OBS: Não criamos um volume em si. Mas apontamos para um diretorio;

    Desta forma o diretorio ficara em sua maquina, sera o volume do container;

    ex: -v D:\Progamas\CompassUol\Sprint_3\Exercicios\docker_desenvolvedores\volumes\messages:/var/www/html/messages


---

<br>

### Criando volumes  <u>Manualmente</u>

    docker volume create <nome>



### Criando volume somente de <u>LEITURA</u> 

    docker run volume -v volume:/dara:ro

    RO -> é abreviação de READ ONLY

    obs: Esse volume so tem permoção de LEITURA.

    ex: -v volumedeleitura:/var/www/html:ro


