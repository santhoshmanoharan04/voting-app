FROM node:16
WORKDIR /app
COPY . .
RUN npm install express pg
EXPOSE 80
CMD [ "node", "app.js" ]