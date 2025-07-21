FROM node:20

RUN apt-get update && apt-get install -y python3 make g++

WORKDIR /app
COPY package*.json ./

RUN rm -rf node_modules package-lock.json

RUN npm install --legacy-peer-deps

COPY . .

CMD ["npm", "run", "dev"]
