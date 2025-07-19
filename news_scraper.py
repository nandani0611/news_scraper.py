import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the HTML content from The Hindu
url = "https://www.thehindu.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Extract headlines
# The Hindu uses <a> tags with class 'story-card75x1-text'
headlines = soup.find_all("a")

# Step 3: Save headlines to a text file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headlines:
        text = headline.get_text(strip=True)
        if text and len(text) > 30:  # Ignore short/unwanted links
            file.write(text + "\n")

print("✅ Headlines saved to 'headlines.txt'")
