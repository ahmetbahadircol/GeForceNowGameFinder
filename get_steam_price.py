import requests
from bs4 import BeautifulSoup


def _prepare_request(game_term: str):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://store.steampowered.com/app/1326470/Sons_Of_The_Forest/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'term': game_term,
        'f': 'games',
        'cc': 'TR',
    }

    return headers, params


def get_game_price_steam(game_name: str):
    headers, params = _prepare_request(game_name)
    response = requests.get('https://store.steampowered.com/search/suggest', params=params, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.findAll("div", {"class": ["match_name", "match_price"]})
    if soup:
        for idx, g in enumerate(soup):
            if idx % 2 != 0:
                continue
            try:
                name = g.contents[0]
                if name == game_name:
                    price = soup[idx + 1].contents[0]
                    return price
            except IndexError as e:
                return None
