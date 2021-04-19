FROM python:3.8

WORKDIR /src
COPY ./GASUScheduleBot/requirements.txt /src
RUN pip install -r requirements.txt
COPY ./GASUScheduleBot /src
