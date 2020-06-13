# Bind /sys directory on the host to /sys container directory
FROM python:3.7-alpine

WORKDIR /usr/src/app

RUN pip install prometheus_client

COPY main.py .

CMD [ "python", "./main.py" ]


