import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import os.path

def check_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def write_to_csv(data, filename):
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Author', 'URL', 'Snippet']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # Only write header if file doesn't exist

        for entry in data:
            writer.writerow(entry)

def scrape_news(URL):
    data = []
    try:
        page = requests.get(URL, timeout=10)
        page.raise_for_status()

        try:
            soup = BeautifulSoup(page.content, "html.parser")
            news_cards = soup.find_all('div', class_='news-card news-headlines-card news-headlines-card-normal')

            for card in news_cards:
                title = card.get('data-title')
                author = card.get('data-author')
                url = card.get('url')
                snippet = card.find('div', class_='news_snpt').text if card.find('div', class_='news_snpt') else 'No snippet available'
                data.append({
                    'Title': title,
                    'Author': author,
                    'URL': url,
                    'Snippet': snippet
                })
        except Exception as e:
            print(f"Error during parsing: {e}")

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Oops: Something Else", err)

    return data

            
def remove_duplicates(filename):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [dict(row) for row in reader]
    
    unique_data = {frozenset(item.items()):item for item in data}.values()

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(unique_data)


if __name__ == "__main__":
    if check_internet():
        today = datetime.now().strftime("%Y%m%d")
        filename = f"{today}Headlines.csv"

        news_data = scrape_news("https://bing.com/news")
        if news_data:
            write_to_csv(news_data, filename)
            remove_duplicates(filename)
        else:
            print("No news data was scraped.")