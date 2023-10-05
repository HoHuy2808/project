import requests
from bs4 import BeautifulSoup
# Request to website and download HTML contents
url = "https://www.boxofficemojo.com/date/2023-09-02/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table', class_="a-section imdb-scroll-table mojo-gutter imdb-scroll-table-styles")
    print(table)