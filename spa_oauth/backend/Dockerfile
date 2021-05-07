FROM python:3.8-slim

COPY . /app
WORKDIR /app

ENV DATABASE_HOST=0.0.0.0
ENV DATABASE_PORT=5432
ENV DATABASE_USER=vadbeg
ENV DATABASE_PASSWORD=password
ENV DATABASE_NAME=database
ENV API_PREFIX=/api/v_0
ENV REACT_APP_ROOT_BACKEND_URI=http://0.0.0.0:9000/api/v_0/
ENV SECRET_KEY=afsdd

ENV GOOGLE_CLIENT_ID=476155838688-163di12pq91fs3tdjht124bp7qn4v3vs.apps.googleusercontent.com
ENV GOOGLE_CLIENT_SECRET=TEpo0WcOs8PGTtrBr_KBNYEj
ENV GOOGLE_DISCOVERY_URL=https://accounts.google.com/.well-known/openid-configuration


RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:$PORT --timeout 720 -w 3 -k gevent wsgi:app