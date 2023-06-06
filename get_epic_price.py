from bs4 import BeautifulSoup
import cloudscraper

url = "https://store.epicgames.com/ru/p/cities-skylines"

scraper = cloudscraper.create_scraper()
response = scraper.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    price_element = soup.find('div', 'css-169q7x3').find(class_='css-119zqif')
    print(price_element)

    if price_element is not None:
        price = price_element.get_text(strip=True) 
        print("Price Cities: Skylines:", price)
    else:
        print("Error")
else:
    print("Error:", response.status_code)