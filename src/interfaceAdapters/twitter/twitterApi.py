from config.settings import (
    TWITTER_TOKEN_URL,
    TWITTER_SEARCH_URL,
    TWITTER_KEY,
    TWITTER_SECRET_KEY,
)
import requests
import base64
import json


def __getAccessToken():
    url = TWITTER_TOKEN_URL
    secretKey = TWITTER_KEY + ":" + TWITTER_SECRET_KEY
    secretKeyBytes = secretKey.encode("utf-8")
    secretKeyEncoded = base64.b64encode(secretKeyBytes)

    headers = {
        "Authorization": "Basic " + secretKeyEncoded.decode("utf-8") + "",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    formParams = {"grant_type": "client_credentials"}

    result = requests.post(url, data=formParams, headers=headers)

    if result.status_code != 200:
        raise Exception("Ocorreu um erro ao obter o token de acesso ao twitter")

    resultJson = result.json()

    return resultJson["access_token"]


def search(hashtags, fromDate, toDate):
    token = __getAccessToken()

    url = TWITTER_SEARCH_URL

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    query = hashtags

    body = json.dumps({"query": query, "fromDate": fromDate, "toDate": toDate})

    result = requests.post(url, data=body, headers=headers)

    return result.json()
