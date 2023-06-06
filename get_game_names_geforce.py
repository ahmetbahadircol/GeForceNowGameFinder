import requests


def get_game_list() -> dict:
    data = '{ apps(country: "US" language: "en_US") {\n        numberReturned\n        pageInfo {\n          endCursor\n          hasNextPage\n        }\n        items {\n        title\n        sortName\n        \n      variants{\n        appStore\n        publisherName\n            }\n        }\n    }\n}'

    headers = {
        'authority': 'api-prod.nvidia.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.nvidia.com',
        'referer': 'https://www.nvidia.com/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }
    link = "https://api-prod.nvidia.com/gfngames/v1/gameList"
    req = requests.post(link, data=data, headers=headers)
    return req.json().get("data").get("apps").get("items")
