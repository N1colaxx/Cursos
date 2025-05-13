
# kubernetes

### O que é ?

    Uma ferramenta de orquestração de containers;

    Ele permite automatizar o deploy, o escalonamento, o monitoramento e a gerência de aplicações containerizadas (como as criadas com Docker), distribuídas em clusters de servidores.

    Ele distribui, inicia, reinicia, escala e organiza os containers conforme necessário, garantindo que suas aplicações estejam sempre rodando da melhor forma possível.

    Mas não interfere diretamente na infraestrutura (como redes ou volumes), diferente do Swarm, que atua mais integrado à infraestrutura Docker.

   ---

### Comparação com o Docker Swarm:

-   Ambos são orquestradores de containers;

-   O Swarm é mais simples e fácil de configurar;

-   O Kubernetes é mais completo, robusto e amplamente adotado em ambientes corporativos e em nuvem.

    ---

### Conceitos Principais

`Control Plane`
-   Comanda o cluster; decide o que, quando e onde rodar os containers (responsável por agendamento, controle e monitoramento).

`Nodes`
-   Máquinas (físicas ou virtuais) que executam os containers. Cada node possui o agente chamado kubelet.

`Deployment`
-   É a forma de executar uma imagem/projeto dentro de um Pod, com gerenciamento automático;
-   Gerencia o deploy e a atualização de Pods de forma declarativa — você descreve o estado desejado (quantos Pods, qual imagem usar, etc.), e o Kubernetes se encarrega de mantê-lo.

`Pod`
-   É a menor unidade que o Kubernetes executa;
-   Cada Pod roda dentro de um Node, que é a máquina (física ou virtual) onde os containers são realmente executados;
-   Um Pod pode conter um ou mais containers (normalmente só 1);
-   Os containers dentro de um Pod compartilham a mesma rede (IP, porta) e armazenamento (volume);
-   Se um Pod "morre", o Kubernetes pode criar outro no lugar, mas não atualiza o Pod existente — por isso usamos Deployments para gerenciar isso.

        Cluster
        └─ Node (máquina física/virtual)
        ├─ Pod A
        │  ├─ Container 1
        │  └─ Container 2
        └─ Pod B
            └─ Container 1

        Legenda de cima para baixo:

            Cluster: conjunto de nodes.

            Node: máquina que executa Pods.

            Pod: unidade mínima, pode ter múltiplos containers.

            Container: aplicação leve, isolada dentro do Pod.


`Services `
-   Expõem os pods para acesso interno ou externo, garantindo comunicação estável mesmo que os pods mudem.

`Kubctl`
-   Ferramenta de linha de comando para interagir com o cluster Kubernetes (deployar, escalar, monitorar, etc).

---

### Iniciando o Minikube

-   **minikube start --driver= DRIVE-NOME**

### Parando o Minikube

-   **minikube stop**

    ---

### Acessando a deshboard do kubernetes

-   **minikube dashboard**

ou apenas obter a URL:
-   **minukube dashboard -url**

---
<br>

## Criar um Projeto (deployment)

-   **kubectl create deployment nome_deploy --image nome_img**

    ---

### Verificando Deployments

-   kubectl get deployments

        Lista todos os deployments existentes no seu cluster Kubernetes. Ele fornece uma visão geral rápida dos deployments, incluindo o número de réplicas e o estado atual deles.

-   kubectl describe deployments

        Fornece informações detalhadas sobre um deployment específico, incluindo o estado dos pods, containers, histórico de atualizações e eventos relacionados ao deployment. Isso é muito útil para diagnosticar problemas, como falhas na criação de pods ou imagens erradas.


-   kubectl get pods 
-   kubectl describe pods 

    ---

### CFG do Kubernetes

-   kubectl config view 

---
<br>

## Criando um Serices

-   kubectl expose deployment nome_deploy --type=nome_tipo --port=N°porta

    `type: `a varios tipos, porem vamos utilisar o **LoadBalancer**, o mais comum onde todos os Pods são expostos.

    ---

### Gerando o ip de acesso

`OBS: `Precisamos fazer isso porque estamos usando o Minikube, já que nosso projeto está sendo executado localmente.

        Minikube é uma ferramenta que cria um cluster Kubernetes local em uma máquina virtual ou diretamente em sua máquina.

        O Minikube é utilizado principalmente em ambientes locais de desenvolvimento, por isso, ao usar o Minikube, você tem a necessidade de expor serviços para poder acessá-los de seu navegador.

-   minikube  service nome_servico

        Desta forma o ip aparece no terminal 

        E uma aba no navegador é  aberta com o projeto

    ---

### Verificando os serviços

-   kubectl describe services/nome-serviço

    --- 

### Replicando/Excalando a Aplivação

-   kubectl scale deployment/nome_servico --replicas=N°replicas

    ---

### Verificar as replicas 

-   kubectl get rs

    ---

### Reduzindo as scalas

- kubectl scale deployment/nome-serviço --replicas=n°-menor

    basta colocar um numero menor do que a qtd atual 

---

### Atualizar a IMG 


`OBS: `

-   O **nome-container** 

    Se refere ao nome do container que está definido dentro do seu deployment — não é o nome do container Docker local, nem do deployment ou pod. É o nome definido na especificação do deployment YAML, geralmente na seção spec.containers.name.

-   A **nova img**

    Tem que ser a mesma img mas uma verção atualizada, então temos que subir uma nova tag no Hub;

`Ai sim podemos atualizar a img: `

- kubectl set image deployment/nome-deploy nome-container=nova-img


---

### Desfazer uma atualização

`Comando para verificar uma atualizaçao `

-   kubectl rollout status deployment/nome-deploy

`Comando para voltar a atualização Errada: `

-kuberctl rollout undo deployment/nome-deploy    

---

### Deletar um serviço 

-   kubectl delete service nome-serciço

`OBS`

    o serviço ainda esta rodando MAS não esta online para os user, ele apenas perdeu a conecxão 


---

### deletando o deployment

- kubectl delete deployment nome-deploy 

---

<br>

# modo declarativo 

guiado por um um arquivo semelhante ao docker-compose;

agora vamos centralizar tudo em um arquivo com todos os comandos, tbm escrito em yaml para o kubenetes 

    ---

### Chaves mais utilisadas

`apiVersion`

    versão utilizada da ferramenta

`kind`

    tipo do arquivo (Deployments, Service)

`metadata`

    descreve algum obj, incerindo a chave 
    
`replicas`

    numero de replicas de Nodes/Pods

`containers`

    definir as especificações de containers: nome e img 

    ---


### Criando o arquivo 

basta criar um yaml.

    ---

### Executando

-   kubectl apply -f nome_arquivo

### parando o deploy por Arquivo 

-    kubectl delete -f nome_arquivo


---


### Criando o Serviço

Criar um arquivo para realizar p service (kind)

Semelhante ao Deployment, mas com uma responsabilidade diferente;


### Iniciando o serviço 

-    kubectl apply -f nome_arquivo

`OBS`

    precisamos obter IP de acesso com **minekube service nome-service**


### Parando o serviço 

-    kubectl delete -f nome_arquivo

---

### Atualizando o Projeto declarativo 

Primeiro:

    Criar a nova verção da img

Segundo:

    apualizar o yaml com a **tag**

Terceiro>

    reinicializar com o apply

---

### unindo os projetos 

Precisamos unir o Deploymente e o Services em um unico arquiv.

ku