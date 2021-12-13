# Redaction App

This redaction app redacts selected words from text, replacing them with *'s. 

## Requirements

Python Version: Python 3.8.8

## Healthcheck Endpoint

The healthcheck Endpoint is used for health monitoring of this particular service.

GET /healthcheck

It will return a 200 response, with a corresponding message if healthy.

## Redact 

POST Request with a BODY in JSON format to a given endpoint.

{
    "Text to Redact": "The text you wish to redact words from. (String)",
    "Redaction Criteria": "The words you wish to redact. [(String), (String), ... , (String)]",
}

RETURNS the following body content as 'application/json'

{
    "RedactedText": "The redacted text; criterion words replaced with *'s",
}

