# Etapa 1: Build da aplicação
FROM node:18-alpine AS build

# Define o diretório de trabalho
WORKDIR /app

# Copia apenas os arquivos de dependência e instala
COPY package*.json ./
RUN npm install

# Copia o restante do projeto
COPY . .

# Gera a versão final do frontend
RUN npm run build

# Etapa 2: Servir o build com Nginx
FROM nginx:alpine

# Copia os arquivos buildados do Vite para a pasta padrão do Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Expondo a porta padrão
EXPOSE 80

# Inicia o Nginx
CMD ["nginx", "-g", "daemon off;"]
