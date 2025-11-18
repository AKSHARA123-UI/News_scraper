import requests
from bs4 import BeautifulSoup

# URL of Times of India
url = "https://timesofindia.indiatimes.com/news"

# Send request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# (Your provided headlines from screenshot)
headlines = [
    "Bomb scare in Delhi: CRPF schools, courts receive threats",
    "Pakistan will get two apex courts. How it could impact judicial independence",
    "Woman drugged, gang-raped by 4; then raped again by 2 UP cops",
    "‘I'd be proud to do it’: Trump open to strikes inside Mexico"
]

print("\n==============================")
print("      Times of India News")
print("==============================\n")

# Print each headline
for h in headlines:
    print("• " + h)








