FROM python:3.11-alpine

#Переменная необходима, например, для запуска только отдельных тестов
#production либо
ARG run_env
ENV env $run_env
LABEL "creator" = "beatacles"

WORKDIR ./usr/lessons

VOLUME /reports_docker

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apk update && apk upgrade && apk add bash

COPY . .
#Вот тут -m "$env"=production
CMD pytest -s -v tests/* --alluredir=reports_docker

#Достаем результаты allure, копируем в окружение
#docker cp $(docker ps -a -q | head -1):/usr/lessons/reports_docker .

