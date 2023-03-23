from bs4 import BeautifulSoup
import requests
import lxml

url = "https://uel.ru/bitrix/catalog_export/pioneer.php"

#r = requests.get(url)
soup = BeautifulSoup(requests.get(url).text, "lxml")

print(soup)