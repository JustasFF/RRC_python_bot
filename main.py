from bs4 import BeautifulSoup
import requests

url = "https://uel.ru/bitrix/catalog_export/pioneer.php"

soup = BeautifulSoup((requests.get(url)).text, features='lxml')
offers2 = []
pioneer = {'': {'url': '', 'price': 0, 'currencyId': '', 'categoryId': '', 'name': '', 'brand': '', 'purpose': ''}}
offers = soup.find_all('offer')
for data in offers:
    if data.find('url'):
        offers2.append(data)
offers2[0] = str(offers2[0])
print(offers2[0])
print(offers2[0].find('id='))
