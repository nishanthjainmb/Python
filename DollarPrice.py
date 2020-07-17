from bs4 import BeautifulSoup
import requests

urllink='https://www.moneycontrol.com/currency/bse-usdinr-price.html?classic=true'

source=requests.get(urllink).text
soup=BeautifulSoup(source,'lxml')
# print(soup.prettify())

money_value=soup.find('span',class_='gr_20')
dollar_value=money_value.strong.text
print('American Dollar=',dollar_value)