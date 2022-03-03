import string
import requests
from bs4 import BeautifulSoup as bs
import re

#LA County
# r = requests.get('https://www.lacourt.org/newsmedia/notices/attorneynotice')
# soup = bs(r.content)
# headers = soup.find_all('tbody')
# table = soup.find('table', attrs={'id': "siteMasterHolder_generalInfoLeftHolder_ctl00_tblAll"})
# notification = table.find('td', string = re.compile("03/01/2022"))
# print(notification)

#Alameda County
# r = requests.get('http://www.alameda.courts.ca.gov/Default.aspx')
# soup = bs(r.content)
# table = soup.find('td', attrs={'class':'bulletLinks'})
# notification = table.find('strong', string = re.compile('2/14/22'))
# print(notification)

#Alpine County
# r = requests.get('https://www.alpine.courts.ca.gov/views/news')
# soup = bs(r.content)
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('October 14, 2021'))
# print(notification)

#Amador County
# r = requests.get('https://www.amadorcourt.org/')
# soup = bs(r.content)
# table = soup.find('div', attrs={'class': "special"})
# notification = table.find('div', string = re.compile('02/25/22'))
# print(notification)

#Butte County
# r = requests.get('https://www.buttecourt.ca.gov/PressInfo/')
# soup = bs(r.content)
# table = soup.find('div', attrs={'class': 'w3-card-2 w3-padding'})
# notification = table.find('p', string = re.compile('November 15, 2021'))
# print(notification)

#Colusa County
# r = requests.get('https://www.colusa.courts.ca.gov/general-information/news')
# soup = bs(r.content)
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('April 20, 2021'))
# print(notification)

#Contra Costa County
# r = requests.get('https://www.contracosta.ca.gov/CivicAlerts.aspx?CID=37')
# soup = bs(r.content)
# table = soup.find('div', attrs={'id': "37"})
# notification = table.find('span', string = re.compile('March 2, 2022'))
# print(notification)