# Comp Vision Language App

The Language App is an application which provides offline translation of text to english. It also identifies unknown languages.

## Requirements

Python Version: Python 3.8.8

## Healthcheck Endpoint

The healthcheck Endpoint is used for health monitoring of this particular service.

GET
/healthcheck

It will return a 200 response, with a corresponding message if healthy.

## Translate Endpoint

Our Translation API utilises the same query style as AWS Translate for consistency across platforms.

POST Request in JSON format to a given endpoint.

{
    "Text": "",
    "SourceLanguageCode": "auto",
    "TargetLanguageCode": "en"
}

RETURNS:

{
    "TranslatedText": "",
    "SourceLanguageCode": "",
    "TargetLanguageCode": ""
}