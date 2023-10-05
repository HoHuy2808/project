import requests
from bs4 import BeautifulSoup
url = "https://www.formula1.com/en/results.html/2023/drivers.html"
response = requests.get(url)
if response.status_code == 200:
    data = BeautifulSoup(response.content, "html.parser")
    table = data.find('table',class_="resultsarchive-table")
    print(table)