# 1. Define a imagem base, que neste caso é a imagem oficial do Node.js.
# O Docker irá baixar essa imagem se ela não estiver presente localmente.
FROM node:alpine


# 2. Define o diretório de trabalho dentro do container.
# Todos os comandos subsequentes (como COPY, RUN, etc.) serão executados nesse diretório.
WORKDIR /src

# 3. Copia os arquivos de dependências do projeto (package.json e package-lock.json ou qualquer arquivo que combine com a regex "package*.json").
# Esses arquivos são copiados para o diretório atual dentro do container (/app).
COPY package*.json .

# 4. Executa a instalação das dependências do Node.js com npm.
# A partir do momento que copiamos o arquivo package.json, precisamos executar 'npm install' para instalar as dependências.
RUN npm install

# 5. Copia todos os outros arquivos do seu projeto para o diretório /app dentro do container.
# Esse comando garante que o código da sua aplicação (arquivos .js, .html, etc.) seja copiado para dentro do container.
COPY . .

# 6. Expõe a porta 3000 do container.
# Isso indica ao Docker que a aplicação dentro do container vai usar a porta 3000 para comunicação.
# Ao rodar o container, você pode mapear essa porta para uma porta do seu computador host.
EXPOSE 3000

# 7. Define o comando que será executado quando o container for iniciado.
# Nesse caso, o Docker executará o arquivo "app.js" usando o Node.js.
CMD ["node", "app.js"]
