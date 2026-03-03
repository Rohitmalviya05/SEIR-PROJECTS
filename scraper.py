import sys
import requests
from bs4 import BeautifulSoup

def page_content(url):
    try:
        response = requests.get(url)
    except:
        print("Error in opening the webpage:", url)
        return None, "", []

    soup = BeautifulSoup(response.text, "html.parser")

    if soup.title:
        title = soup.title.get_text()
    else:
        title = "No Any title found"

    if soup.body:
        body = soup.body.get_text()
    else:
        body = ""

    links = []
    for tag in soup.find_all("a"):
        href = tag.get("href")
        if href:
            links.append(href)
    return title, body.lower(), links

# Main
if len(sys.argv) < 2:
    sys.exit(1)
urls = sys.argv[1:]
for url in urls:
    print("Giving for:", url)
    title, body, links = page_content(url)
    print("Title is:", title)
    print("Body of  the Web:\n", body[:500])
    print("Links :")
    for link in links[:10]:
        print(link)