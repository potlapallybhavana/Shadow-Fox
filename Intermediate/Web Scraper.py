"""
Intermediate Task 1: Web Scraper
Usage:
    python scraper.py "https://example.com"
Extracts page title and all anchor texts + hrefs and writes to links.csv
"""
import sys, csv
from pathlib import Path
import requests
from bs4 import BeautifulSoup

def scrape(url: str, out_csv="links.csv"):
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    title = (soup.title.string.strip() if soup.title and soup.title.string else "")
    links = []
    for a in soup.select("a[href]"):
        text = (a.get_text(strip=True) or "")
        href = a["href"]
        links.append({"text": text, "href": href})
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "href"])
        writer.writeheader()
        writer.writerows(links)
    return title, out_csv, len(links)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scraper.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    title, out_csv, n = scrape(url)
    print("Page title:", title)
    print("Saved", n, "links to", out_csv)
