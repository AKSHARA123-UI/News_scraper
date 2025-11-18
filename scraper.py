import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Get today's date
today = datetime.now().strftime("%d-%m-%Y")

# Business section URL
url = "https://timesofindia.indiatimes.com/business"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Collect headlines from multiple patterns
headlines = []

# Pattern 1
headlines += [h.get_text().strip() for h in soup.find_all("span", class_="w_tle")]

# Pattern 2 (backup)
headlines += [h.get_text().strip() for h in soup.find_all("h2")]

# Clean duplicates and empty text
cleaned = []
for h in headlines:
    if h not in cleaned and len(h) > 5:
        cleaned.append(h)

# Print date
print(f"\nTop Times of India Business Headlines ({today})\n")

# Show first 12 headlines
for index, headline in enumerate(cleaned[:12], start=1):
    print(f"{index}. {headline}")










