
# Conectando container com NERWORKS 

### `O que é Networks no Docker ?`

-   Uma forma de gerenciar a conexão do Docker com outras plataformas ou ate mesmo entre containers.

-   As resdes ou nerworks são criadas semparadas dos containers, como os volumes.


### `Quais os tipos de CONEXÃO` ? 

Tem 3 principais tipos:

-   **Externa:** conexão com API de um servidor remoto;

-   **Com o host:** comunicação com a maquina que esta executando o Docker;

-   **Entre container:** comunicação que utiliza o drive bridge e permite a comunicação entre 2 ou mais containers;


### `Tipos de rede (drivers)`

-   **bridge:** Rede padrão para contêineres em um host, isolada, com NAT para acesso externo.

-   **host:** Contêiner compartilha a rede do host, sem isolamento de IP/porta.

-   **macvlan:** Atribui um endereço MAC ao contêiner, permitindo que ele apareça como um dispositivo físico na rede.

-   **none:** Remove todas as interfaces de rede do contêiner, oferecendo total isolamento de rede.

-   **plugins:** Permite redes personalizadas criadas por plugins de terceiros para casos avançados (ex: redes SDN).


--- 

docker **network ls**

    Lista as redes do nosso ambiente de desenvolvimento. 




docker **network create nome_para_rede**

    Cria uma rede.

    OBS: essa rede sera do tipo BRIDGE




docker **network -d nome_drive nome_para_rede**

    Esse comando cria uma rede com um DRIVE em  expecifico.




docker **network rm nome_rede**

    Esse remove a rede .

    Desconecta tudo que esta conectado na rede.




docker **network prone**

    Remove as resdes que não esta em execução.


---

<br>

# Comandos de Conexão 


`Conecxão com **maquina HOST**`

    docker run -d -p 5000:5000 --name flask_container --rm --network flasknetwork flaskapinetwork


`Conecxão **entre CONTAINER**`

    docker run -d -p 3306:3306 --name mysql_api_container --rm --network flasknetwork -e MYSQL_ALLOW_EMPTY_PASSWORD=true flaskimgmsql
    
    docker run -d -p 5000:5000 --name flask_api_container --rm --network flasknetwork flaskapinetwork


    obs :

    --network flasknetwork: Garante que ambos os containers estão na mesma rede Docker, permitindo que eles se comuniquem usando o nome do container (ex: mysql_api_container como hostname no Flask).

    -e MYSQL_ALLOW_EMPTY_PASSWORD=true: Permite que o container MySQL aceite login do usuário root sem senha. Isso é útil para testes, mas não é seguro em produção.


`Conectar um container a uma rede`

    docker network connect nome_rede nome_container
    
    ex: docker network connect flasknetwork 895bd5d4bc37
    

`Remover um container de uma rede`

    docker network disconnect nome_rede nome_container
    
    ex: docker network disconnect flasknetwork 895bd5d4bc37


`Inspencionar uma Rede`

    docker network inspect nome_rede

    ex: docker network inspect flasknetwork
    
---