import requests
from bs4 import BeautifulSoup


def request_data():
    return {
        "referrer": "https://www.nvidia.com/",
        "referrerPolicy": "strict-origin-when-cross-origin",
        "body": "{ apps(country:\"US\" language:\"en_US\") {\n        numberReturned\n        pageInfo {\n          endCursor\n          hasNextPage\n        }\n        items {\n        title\n        sortName\n        \n      variants{\n        appStore\n        publisherName\n          }\n        }\n}}",
        "method": "POST",
        "mode": "cors",
        "credentials": "omit"
    }


def get_game_list():
    body = """{ apps(country:"US" language:"en_US") {\n        numberReturned\n        pageInfo {\n          endCursor\n          hasNextPage\n        }\n        items {\n        title\n        sortName\n        \n      variants{\n        appStore\n        publisherName\n          }\n        }\n}}""",

    headers = {
        "referrer": "https://www.nvidia.com/",
        "referrerPolicy": "strict-origin-when-cross-origin",
        "method": "POST",
        "mode": "cors",
        "credentials": "omit",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json;charset=UTF-8",
        "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site"
    }
    link = "https://api-prod.nvidia.com/gfngames/v1/gameList"
    req = requests.post(link, data=body, headers=headers)
    # soup = BeautifulSoup(r.text, "html.parser")
    # soup = soup.findAll("div", {"class": "main-container"})
    # print(soup[0].find_all("div"))
