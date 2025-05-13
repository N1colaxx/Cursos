
git hub:> https://github.com/matheusbattisti/curso_docker


# Manipulação Docker:



docker **run nome_img**

    Verifica se a imagem existe localmente.
    Se não tiver, faz o pull (download).
    Executa o container em primeiro plano (mostra logs no terminal).

    

docker **run -it  nome_img** 

    Executa o container em modo interativo com terminal aberto (ideal para shells).



docker **ps** OR **conainer ls**

    Mostea os cantainer em execução 


docker **ps** OR **conainer ls** COM FALG **-a**

    Mostra os cantainer em execução e que ja foram executados 



docker **run -d  nome_img** 

    Executa o container em modo "detached" (segundo plano, background).
    Não trava seu terminal.



docker **run -d -p x:x**

    -d (opcional): Executa o container em segundo plano (background).

    -p: Faz o mapeamento de portas, ou seja, expõe uma porta do container para ser acessada pela porta do seu computador (host).

    Troque o x:x pela porta -> 80:80

    A primeira porta é do PC
    A segunda porta do Serviço (container)


docker **stop nome_container ou ID_container**

    Encerra a execução de um container em andamento.



docker **start nome_container ou ID_container**

    Inicia a execução de um container emque estava Parado ou Interrompido



docker **run -d -p --name nome_container**

    -d -p (opcional)

    --name -> vc define o nome que o container vai ter 



docker **logs nome_container or id_container** 

    Acessa os logs do container especificado, mostrando as saídas anteriores geradas durante sua execução.

    preferencia pelo ID


docker **logs -f nome_container or id_container** 

    Acessa os logs do container em tempo real, permitindo acompanhar as novas saídas à medida que são geradas.

    preferencia pelo ID


docker **rm nome_container or id_container**

    Remove o container da máquina.

    OBS: Não é possível remover containers em execução. Você precisa parar o container antes de removê-lo.

docker **rm name or id  do container -f**

    Remove o container da máquina, mesmo que ele esteja em execução.

    OBS: Usa a flag -f para forçar a remoção, independentemente do status do container.

---

<br>
<br>


### Criando Imagens Docker:

1. **Arquivo**
    - Crie um arquivo chamado `Dockerfile`, que contém as instruções para construir a imagem Docker.

2. **Instruções**
    - Dentro do `Dockerfile`, insira as instruções que definem o funcionamento da imagem e como ela será configurada.

3. **FROM**
    - Define a imagem base a ser usada. Por exemplo, `FROM ubuntu` ou `FROM node:14`.

4. **WORKDIR**
    - Define o diretório de trabalho dentro do container onde a aplicação será executada. Exemplo: `WORKDIR /app`.

5. **EXPOSE**
    - Exponha a porta que a aplicação irá usar. Exemplo: `EXPOSE 80` para expor a porta 80.

6. **COPY**
    - Copia arquivos ou diretórios do sistema de arquivos local para o sistema de arquivos do container. Exemplo: `COPY . /app` para copiar o conteúdo do diretório atual para o diretório `/app` dentro do container.


---

<br>

### Rodando IMG que eu criei 


docker **build .**

    Comando para construir uma imagem a partir de um Dockerfile.
    OBS: O ( . ) tem q ser separodo do build, ex: (build .)


docker **build  -t nome_img .**

    Comando para construir a img com um nome de SUA AUTORIA 


docker **image ls**

    Exibe todas as imagens existentes no seu sistema Docker

    OBS: parecido com o container ls



Docker **rmi E rm + id_img**
   
    rm -> deleta o container
    rmi -> deleta a img do seu PC. 
    OBS: mas o não pode conter um container rodando ou parado. 

    

docker **system prune**

    remove todos os recursos não utilizados pelo Docker, incluindo:

    containers parados

    imagens não referenciadas (dangling)

    redes não utilizadas

    volumes anônimos (somente com --volumes)

-   `Esse comando libera espaço no seu sistema, mas cuidado: ele pode apagar dados importantes se você tiver volumes com dados persistentes ou imagens temporárias que ainda pretende usar.`


docker **inspect id or name container**

    Exibe todas as informações detalhadas sobre um container (ou imagem, volume, rede, etc), em formato JSON estruturado.



docker **stats id or name container**

    Se quiser ver uso de recursos em tempo real.


---

<br>






