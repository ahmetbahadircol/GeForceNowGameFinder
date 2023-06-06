from get_game_names_geforce import get_game_list
from get_steam_price import get_game_price_steam
import time


PRICE_GETTER_BASED_ON_PLATFORM = {"STEAM": get_game_price_steam, "UPLAY": None, "EPIC": None}


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


if __name__ == "__main__":
    start = time.time()

    get_game_price()

    end = time.time()
    print(f"Execution time: {(end - start)}")
