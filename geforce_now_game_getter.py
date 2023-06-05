import requests
from get_steam_price import get_game_price_steam


PRICE_GETTER_BASED_ON_PLATFORM = {"STEAM": get_game_price_steam, "UPLAY": None, "EPIC": None}


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


def get_game_price():
    game_list = get_game_list()
    for idx, game_dict in enumerate(game_list):
        _title = game_dict.get('title').replace("®", "").replace("™", "")
        app_store = [store.get("appStore") for store in game_dict.get("variants")]
        price_based_on_store = dict()

        for platform in app_store:
            price_getter = PRICE_GETTER_BASED_ON_PLATFORM.get(platform)
            if price_getter:
                _price = price_getter(_title)
                price_based_on_store[platform] = _price
            else:
                price_based_on_store[platform] = None

        _steam_price = price_based_on_store.get("STEAM")
        _epic_price = price_based_on_store.get("EPIC")
        print(f"{idx+1} - {_title} - STEAM: {_steam_price}, EPIC GAMES: {_epic_price}")
