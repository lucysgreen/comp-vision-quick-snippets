# Comp Vision Language App

The Language App is an application which provides offline translation of text to english. It also identifies unknown languages.

## Requirements

Python Version: Python 3.8.8

## Healthcheck Endpoint

The healthcheck Endpoint is used for health monitoring of this particular service.

GET /healthcheck

It will return a 200 response, with a corresponding message if healthy.

## Translate to English Endpoint

Our Translation API utilises the same query style as AWS Translate for consistency across platforms.

POST Request with a BODY in JSON format to a given endpoint.

{
    "Text": "The text you wish to translate as string.",
    "SourceLanguageCode": "The language of the string you with to translate to engish, as string, OR THE WORD (AS STRING): auto",
    "TargetLanguageCode": "en"
}

RETURNS the following body content as 'application/json'

{
    "TranslatedText": "The Translated Text as string",
    "SourceLanguageCode": "The ISO language code for source translation as string. If originally selected 'auto', this will return the detected language code.",
    "TargetLanguageCode": "The ISO language code for the target translation as string. This will always be en - English."
}

## Identify Language

POST Request with BODY in JSON Format to endpoint: /identify

{
    "Text": "Text as string. More text lends a far more reliable result."
}

RETURNS the following body content in application/json:

{
    "Text": "Original text as string",
    "LanguageName": "Full name of language as string",
    "LanguageCode": "ISO Language code as string",
    "IsReliable": Is this result reliable? as bool true or false,
    "ProportionTextWithLanguage": Proportion of text including identified language, as int,
    "Probability": Percentage probability of language match, as int.
}

## Get Languages Endpoint

GET Request to endpoint: /source-languages

RETURNS the following body content in application/json:

    ["List", "Of", "Languages", "As", "Strings"]
