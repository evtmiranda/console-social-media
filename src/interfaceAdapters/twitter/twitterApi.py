from config.settings import TWITTER_TOKEN_URL, TWITTER_SEARCH_URL, TWITTER_KEY, TWITTER_SECRET_KEY
import requests
import base64


def __getAccessToken():
    url = TWITTER_TOKEN_URL
    secretKey = TWITTER_KEY + ":" + TWITTER_SECRET_KEY
    secretKeyBytes = secretKey.encode('utf-8')
    secretKeyEncoded = base64.b64encode(secretKeyBytes)

    headers = {
        "Authorization": "Basic " + secretKeyEncoded,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    formParams = {"grant_type": "client_credentials"}

    result = requests.post(url, data=formParams, headers=headers)

    return result.access_token


def search(hashtags, fromDate, toDate):
    token = __getAccessToken()

    url = TWITTER_SEARCH_URL

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    query = hashtags

    body = {
        "query": query,
        "fromDate": fromDate,
        "toDate": toDate
    }

    result = requests.post(url, data=formParams, headers=headers)

    return result
