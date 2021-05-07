FROM node:13.12.0-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

ENV DATABASE_HOST=0.0.0.0
ENV DATABASE_PORT=5432
ENV DATABASE_USER=vadbeg
ENV DATABASE_PASSWORD=password
ENV DATABASE_NAME=database
ENV API_PREFIX=/api/v_0
ENV REACT_APP_ROOT_BACKEND_URI=https://spa-vadbeg-back.herokuapp.com/api/v_0/
ENV SECRET_KEY=afsdd

ENV GOOGLE_CLIENT_ID=476155838688-163di12pq91fs3tdjht124bp7qn4v3vs.apps.googleusercontent.com
ENV GOOGLE_CLIENT_SECRET=TEpo0WcOs8PGTtrBr_KBNYEj
ENV GOOGLE_DISCOVERY_URL=https://accounts.google.com/.well-known/openid-configuration

COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g

COPY . ./

CMD npm start -- --port $PORT