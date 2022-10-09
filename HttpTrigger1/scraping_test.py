from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import json
import requests
from bs4 import BeautifulSoup

URL = "https://ekosystem.wroc.pl/wp-admin/admin-ajax.php"
FORM_DATA = {"action": "waste_disposal_form_get_schedule_direct",
             "id_numeru": 45429, "id_ulicy": 1791}

page = requests.post(URL, FORM_DATA).json()["wiadomosc"]

elements = page.split("kiedy")[1:]

for i in elements:
    print(i)

# soup = BeautifulSoup(page.content, "html.parser")

# result = soup.find(href=True)["href"]

# print(result)
