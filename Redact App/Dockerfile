FROM python:3.8.8-buster

LABEL version="1.0.0"
LABEL description="Redaction App"

EXPOSE 5001

WORKDIR /

COPY . .

RUN apt update && apt upgrade -y
RUN apt install gunicorn protobuf-compiler -y
RUN pip3 install -r requirements.txt

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]