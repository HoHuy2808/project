import requests
import json
from bs4 import BeautifulSoup
# Request to website and download HTML contents
def boxOfficeMojo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    rows = soup.find_all('tr')

    for row in rows[1:]:
        rank = row.find('td',{'class':'mojo-header-column'}).text
        nameMovie = row.find('td',{'class':'mojo-field-type-release'}).text
        revenue = row.find('td',{'class':'mojo-field-type-money'}).text
        gross_change_by_date = row.find('td',{'class':'mojo-field-type-percent_delta'}).text
        studio = row.find('td',{'class':'mojo-field-type-release_studios'}).text.replace('\n',"")
        
        data = {"Rank": rank,"Name": nameMovie,"Revenue": revenue,"Gross Change": gross_change_by_date, "Studio": studio}
        final_data = json.dumps(data, indent=4)
        return final_data
url = "https://www.boxofficemojo.com/date/2023-09-02/"
boxOfficeMojo(url)
