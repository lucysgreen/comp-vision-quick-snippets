FROM python:3.8.8-buster

LABEL version="1.0.0"
LABEL description="Comp Vision - Language App"

ENV FLASK_ENV production

EXPOSE 5001

WORKDIR /

COPY . .

RUN apt update && apt upgrade -y
RUN apt install gunicorn -y
RUN pip3 install -r requirements.txt

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]