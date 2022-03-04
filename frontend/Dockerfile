FROM node


WORKDIR /app

COPY frontend/package.json /app/

RUN npm install
RUN npm install -g @vue/cli

COPY . /app/
