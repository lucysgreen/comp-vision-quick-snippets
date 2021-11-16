# Comp Vision API Gateway

The API Gateway is an application which interfaces with all other microservices.

## Healthcheck Endpoint

The healthcheck Endpoint is used for health monitoring of this particular service.

GET
/healthcheck

It will return a 200 response, with a corresponding message if healthy.

## Translate Endpoint

Our Translation API utilises the same 

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

### Posting Images to our API.

Code Snippet - Python

import os
url = 'http://host:port/endpoint'
with open(path_img, 'rb') as img:
  name_img= os.path.basename(path_img)
  files= {'image': (name_img,img,'multipart/form-data',{'Expires': '0'}) }
  with requests.Session() as s:
    r = s.post(url,files=files)
    print(r.status_code)