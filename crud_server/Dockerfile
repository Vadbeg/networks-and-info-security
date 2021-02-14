FROM python:3.8-slim

COPY . /app
WORKDIR /app

ENV FLASK_APP=start_app.py
ENV FLASK_ENV=development

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT flask init-db && \
    python3 add_questions.py && \
    bash deploy/run_api.sh