
# News Scraper Program

## Description
This News Scraper Program automates the process of gathering the latest news headlines from Bing News. It extracts key information such as the title, author, URL, and a brief snippet for each article. Designed for efficiency and organization, it's an ideal tool for those wanting to keep a record of daily news.

## Features
- **Internet Connection Check**: Ensures an active internet connection before starting the scraping process.
- **News Scraping**: Collects news from Bing News, focusing on news cards.
- **CSV Output**: Saves scraped news data into a CSV file named with the current date (format: 'YYYYMMDDHeadlines.csv').
- **Duplicate Removal**: Checks and removes duplicate entries in the CSV file to maintain unique data.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/DrFaustest/27-web-scraping-news-headlines
   ```
2. Install required Python packages:
   ```
   pip install requests beautifulsoup4
   ```

## Usage
To run the script, execute:
```
python main.py
```
The script will scrape the current day's news from Bing News and store it in a CSV file in the script's directory.

## Dependencies
- Python 3
- `requests`
- `BeautifulSoup`
- `csv`
- `datetime`
- `os.path`

## Error Handling
The program includes comprehensive error handling for network issues and parsing errors, providing user feedback for various exceptions.

## Developer Notes
- Ensure compliance with Bing News's terms of service and scraping policies.
- Intended for educational and personal use, not for commercial distribution.

## Version
- Version 1.0: Initial release.

---
