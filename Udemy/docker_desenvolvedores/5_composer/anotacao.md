# Composer

-   Ferreamenta para rodar multipos conteiners.

-   Apenas 1 arquivo de cfg

-   Uma forma de rodar multiplos **BUILDS e RUNS** com um comando 

-   Em projetos grandes é essencial. 

---

### Rodando Coposer

-   **docker-compose up**

        isso faz as instruções dos arquivos executadas.

-   **docker-compose up -d**

    A opção -d significa "detached mode", ou seja, modo em segundo plano.

-   **docker-compose down**

    Esse comando derruba e remove tudo o que o docker-compose up criou:

    Para os containers.

    Remove a rede criada.

    Remove os volumes anônimos (mas não os volumes nomeados, como db_data, a menos que especifique --volumes).


--- 