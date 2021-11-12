FROM python:3.8.5-buster

LABEL version="1.0.0"
LABEL description="Comp Vision - API Gateway"

ENV FLASK_ENV production

EXPOSE 5000

WORKDIR /

COPY . .

RUN apt update && apt upgrade -y
RUN apt install gunicorn -y
RUN pip3 install -r requirements.txt

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]