FROM node
WORKDIR /code
COPY frontend/package.json /code/
RUN npm install
RUN npm install -g @vue/cli
COPY ./frontend /code/
