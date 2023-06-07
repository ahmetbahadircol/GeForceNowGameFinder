from bs4 import BeautifulSoup
import cloudscraper
from utils import convert_url_suitable


def _prepare_request(game_name: str):
    game_name = convert_url_suitable(game_name)
    url = f"https://store.epicgames.com/en-US/p/{game_name}"
    print(url)
    scraper = cloudscraper.create_scraper()
    return scraper.get(url)


def get_game_price_epic(game_name: str):
    response = _prepare_request(game_name)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check for game detail page is directly accessible
    is_not_found_or_age_limit = soup.find("h1", "css-1gty6cv")

    if is_not_found_or_age_limit:
        is_found = soup.find("h1", "css-1gty6cv").get_text() != "Page Not Found"
    else:
        is_found = True

    if is_found:
        try:
            price_element = soup.find('div', 'css-169q7x3').find(class_='css-119zqif')
        except AttributeError:
            return "Unavailable"

        if price_element is not None:
            price = price_element.get_text(strip=True)
            return price
    return None
