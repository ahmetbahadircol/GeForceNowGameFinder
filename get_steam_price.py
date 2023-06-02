import requests

def prepare_request(game_term: str):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'steamCountry=TR%7C59fc48c1ab53191fc67be2bc1a73af20; browserid=3058553419775486659; sessionid=f0a710149b6672b9039de1ab; timezoneOffset=10800,0; _ga=GA1.2.1414314939.1685690741; _gid=GA1.2.1434797678.1685690741; recentapps=%7B%221326470%22%3A1685690745%7D; app_impressions=2292130@1_7_15__13|2292080@1_7_15__13|1316600@1_7_15__13|1040420@1_7_15__13',
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

    response = requests.get('https://store.steampowered.com/search/suggest', params=params, headers=headers)

    print(response.text)

prepare_request("Panzer Corps 2")