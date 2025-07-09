import requests
from bs4 import BeautifulSoup

def fetch_articles(urls):
    articles = []
    headers = {"User-Agent": "Mozilla/5.0"}  # mimic browser

    for url in urls:
        try:
            page = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(page.content, "html.parser")
            paragraphs = soup.find_all("p")
            text = " ".join(p.get_text() for p in paragraphs)
            title = soup.title.string.strip() if soup.title else "Untitled"
            articles.append({"title": title, "text": text})
        except Exception as e:
            print(f"Error scraping {url}: {e}")
    return articles
