FROM node:18

# Instale build tools
RUN apt-get update && apt-get install -y python3 make g++

WORKDIR /app
COPY package*.json ./

# Remova o lockfile e node_modules para evitar bugs
RUN rm -rf node_modules package-lock.json

# Reinstale os pacotes
RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
