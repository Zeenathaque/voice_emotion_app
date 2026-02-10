import requests
from bs4 import BeautifulSoup

def scrape_bbc_headlines():
    """
    Scrapes top headlines from BBC News homepage.
    """
    url = "https://www.bbc.com/news"

    try:
        # Send GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find headline elements (BBC uses 'gs-c-promo-heading__title' class)
        headlines = soup.find_all("h2", class_="gs-c-promo-heading__title")

        # Extract and clean headline texts
        top_headlines = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

        print("\n📰 Top BBC News Headlines:\n" + "-" * 40)
        for i, title in enumerate(top_headlines[:10], start=1):  # Show only top 10
            print(f"{i}. {title}")

    except requests.exceptions.RequestException as e:
        print("❌ Error fetching data:", e)


if __name__ == "__main__":
    scrape_bbc_headlines()
