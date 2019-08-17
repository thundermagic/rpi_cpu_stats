# Bind /sys directory on the host to /sys container directory
FROM arm32v7/python:3.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]



