
# Docker Swarme 


### Maneira de execuratar 

-   AWS
-   Docker Labs

    ---



### 🔧 Termos técnicos do Docker Swarm explicados

`Node`
-   **O que é ?**

    Um computador (físico ou virtual) que faz parte do Swarm	
    
-   **Exemplo**

    Pode ser o seu PC ou uma VM, configurado para participar do cluster
    
    ---

`Manager Node`
-   **O que é ?**
    
    Node responsável por controlar e orquestrar o Swarm	É o "chefe" do Swarm. 
    
-   **Exemplo**
    
    Pode criar serviços, escalar, etc.

    ---

`Worker Node`
-   **O que é ?**

    Node que executa os containers, mas não gerencia	

-   **Exemplo**
    
    Só "trabalha", recebe ordens do manager

`Service`	
-   **O que é ?**

    Uma definição de como o container deve rodar no Swarm	
    
-   **Exemplo**

    A imagem, quantidade de réplicas, porta, etc.

`Task`	
-   **O que é ?**

    É uma unidade de execução do Docker Swarm.

    A ordem que o Swarm cria para realizar uma réplica do serviço.

    Em termos práticos: uma task representa a criação de 1 container.

    Container: o resultado da task — o que realmente roda

-   **Exemplo:**
    
    Se você replica 3 vezes um serviço, terá 3 tasks, que gera 3 containers individuais rodando o mesmo serviço.

    Services -> Taks -> container

    1 task = 1 container

`Overlay Network`	
-   **O que é ?***
    
    Rede virtual entre os nodes do cluster.
	
-   **Exemplo:**
    
    Permite comunicação segura entre containers espalhados

`Stack`	
-   **O que é?**
    
    Um conjunto de serviços definidos por um docker-compose.yml	
-   **Exemplo:**
    
    É como rodar um docker-compose, mas no Swarm

---
<br>

# Comandos


### iniciando o Swarm

-   docker **swarm init**

    `Rodar dentro:`  Um node que vai ser Manege 

    Em alguns caso ira ser preciso o uso do IP do server com a flag: **--advertise-addr  n°_ip**

    Isso fara com que a instancia da maquina vire um Node;

    Esse sera seu Node em **Maneger** o "chefe."  

    ---

### Listando Nodes ativos 

-   docker **node ls**

    `Rodar dentro do:` Manager

    Exibe todos os nós que estão participando do cluster Swarm (tanto gerentes quanto workers)

    ---


### ADD novos Nodes

-   docker **swarm join --token TOKEN IP:PORTA**

    `Comando executado` em nodes secundários (workers ou managers) para se juntar ao cluster Swarm já existente.

    Voce entra no Node work e roda esse comando, assim ele fica conequitado ao Manege.

    ---

### Subindo/Criando novo Serviço

-   docker **service create --name nome_serviço nome_img**

    `Rodar dentro do:` Manager

    Cria um serviço gerenciado pelo Swarm, que pode ser replicado automaticamente.

    ---

### listando serviço 

-   docker **service ls**

    `Rodar dentro do:` Manager

    Lista todos os serviços que inicializamos

    ---

### Subindo/Criando novo Serviço com + replicas 

-   docker **service create --name nome_img --replicas numero nome_img**

    `Rodar dentro do:` Manager

    Esse comando cria um serviço no Swarm e define o número de réplicas (instâncias) que o serviço terá.

-   O que acontece:

        O Swarm cria as réplicas (tasks) do serviço e as distribui entre os nodes disponíveis, geralmente nos workers.

        Cada réplica é um container executando o mesmo serviço.

    ---


### Removendo serviço

-    docker **service rm nome or id**

        `Rodar dentro do:` Manager

        Esse comando remove um serviço ativo no Swarm. 

        **O que acontece:**

            Todos os containers associados a esse serviço são imediatamente encerrados e removidos.

            Não ficam pausados nem parados no sistema — são deletados completamente.

            Isso faz parte da responsabilidade do Swarm em manter o estado desejado: se o serviço não existe mais, nenhuma task/container relacionado a ele deve existir também.

        ---


### Verificando a orquestração

-   Vamos remover um container do Node Worker;

        Entra num node worker

        E remove manualmente um dos containers com:

        docker container rm -f <id-do-container>

-    que o Swarm faz ?
    
    O manager detecta que um container (task) foi finalizado.

    Ele entende que o serviço está com uma réplica a menos do que o desejado.

    Então, o Swarm automaticamente cria uma nova task para repor a que foi perdida.

    Essa nova task vai criar um novo container, talvez no mesmo node ou em outro disponível

-   Isso acontece porcalsa do Swarm e uma de suas funções principais:

    <u>**Garantir alta disponibilidade e manter o estado desejado dos serviços**</u>

    Pois o serviço ainda esta rodando no Maneger;

    ---


###  Checando token do Swarm

-   docker **docker swarm join-token menager**
    
    Rodar isso dentro do Manege.

    Assim recebemos o token pelo terminal para poder, dar o join em alguma outra  instancia futuramente;

    Pois nem sempre temos o token igual o fornecido pelo labs.

    ---

### Checando o Swarm

-   docker **info**

    Fornece informações detalhadas sobre o ambiente Docker, incluindo o estado do Swarm quando aplicável.

    ---


### Removendo Instancia do Swarm 

-   docker **swarm leave**

-   docker **swarm leave --force**


    `Executando:` No próprio node: no work ou manege.

    `O que faz:` O node sai por conta própria do cluster Swarm.

    `OBS:` Pode ser usado com --force caso o node seja manager e não consiga sair normalmente.

    Desta maneira  a instancia não é contada mais como um node para o Swarme;
    
    `Containers do Swarm:` (services/tasks) são removidos.

    `Containers locais:` No entanto, (não relacionados ao Swarm) continuarão rodando nesse node, já que o Swarm não interfere nos containers locais.

    ---

### Removendo um Node 

-   docker **node rm id**
-   docker **node rm --force node-id**  # se ainda está ativo


    `Executando:` Usado no manager para remover um node do cluster.

    `O que faz:` Serve especialmente para remover nodes offline ou com falha.

    `OBS:` Só remove um node que já deixou o Swarm (swarm leave) — ou você precisa forçar com --force.

    Desta maneira a instancia não sera mais um Node, saindo do Swarm;

    `Containers do Swarm:` (services/tasks) são removidos.

    `Containers locais:` No entanto, (não relacionados ao Swarm) continuarão rodando nesse node, já que o Swarm não interfere nos containers locais.

    ---
    
### Inspencionado serviços

-   docker **service inspect id**

    Esse comando exibe informações detalhadas sobre um serviço do Swarm.

    O output é em formato JSON.

    ---

### Verificando containers ativado pelo sevice.

-   docker **service pd ID_serviço

    Mostra as tasks (containers) que estão sendo executadas ou que ja deram baixa como parte do serviço.

    ---

### Rodando Compose com Swarm

-   docker **stack deploy -c arquivo-compose.yml nome-stack**

    `Rodar dentro do:` Manege

    Esse comando é usado para subir uma aplicação multi-serviço no modo Swarm, usando um arquivo docker-compose.yml.

    Ele cria uma stack, que é um conjunto de serviços definidos no YAML.

    Os serviços passam a ser gerenciados pelo Swarm, com suporte a réplicas, balanceamento de carga, redes, etc.

    ---

### Excalando a aplicação

-    docker **service scale NOME=REPLICAS**

    `Rodar dentro:` Manager

    Esse comando é usado para aumentar ou diminuir o número de réplicas de um serviço já existente no Swarm.

-   **O que acontece:**

    Ao executar esse comando, o número de tasks (containers) do serviço será ajustado.

    O Swarm distribuirá as novas réplicas entre os worker nodes disponíveis.

    As réplicas adicionais são tasks que são executadas em máquinas diferentes, **`se necessário`**, garantindo balanceamento e alta disponibilidade.

    ---

### Deixar um Node Indisponivel para novas Tasks

-   docker **node update --availability drain ID_node**

   ` Rodar em:` Manager

-   **O que esse comando faz:***

    Marca o Node como indisponível para receber novas Tasks.

    O Docker Swarm migra todas as tasks em execução nesse Node para outros Nodes disponíveis no cluster (se possível).

    O Node continua fazendo parte do cluster, mas não recebe mais containers (tasks) enquanto estiver em estado drain.

        ⚠️ Importante: Esse Node ainda pode ser removido ou modificado manualmente via comandos no Manager, mas ele não será mais utilizado pelo Swarm para agendamento automático de tarefas até que volte para o estado active.

    --- 


### Atualiszar parametro

-   docker **service update --image nome_img nomeOUid_serviço

    `Roda no: ` Maneger

-   **OBS:** 
    
    Não serve apenas para atualizar a imagem — ele pode ser usado para mudar diversos parâmetros de um serviço já criado no Swarm.

-   **Atenção :**

    Somente Nodes em estado ACTIVE recebem as novas tasks.

    Sempre que você atualiza algum parâmetro, o Swarm reinicia as tasks do serviço com as novas configurações (sem downtime, ele faz isso em rolling update).

    Pode ser necessário especificar a versão correta da imagem (ex: nginx:1.25.0) para evitar que ele use a mesma já em cache.

    ---

### Criando redes para Swarm

A conecção entre instancias (containers) usa um driver diferente, **OVERLAY**

`Executar em:` Node Manager

-   Primeiramente criar a rede com:

        docker network create --driver overlay nome_rede

-   Agora criar o serviço conectado a essa rede.

        docker service create --name meu_servico --network nome_rede nome_da_imagem

    ---

### Conectar a um Serviçõ ja criado

`Onde rodar:` No Manager

-   docker **service update --network-add nome_rede nome_servico**

Este comando conecta um serviço já existente a uma rede overlay. Isso permite que o serviço se comunique com outros containers ou serviços que estejam na mesma rede.














