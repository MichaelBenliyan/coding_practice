import string
import requests
from bs4 import BeautifulSoup as bs
import re


#Alameda County
# r = requests.get('http://www.alameda.courts.ca.gov/Default.aspx')
# soup = bs(r.content, features="lxml")
# table = soup.find('td', attrs={'class':'bulletLinks'})
# notification = table.find('strong', string = re.compile('2/14/22'))
# print(notification)

#Alpine County
# r = requests.get('https://www.alpine.courts.ca.gov/views/news')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('October 14, 2021'))
# print(notification)

#Amador County
# r = requests.get('https://www.amadorcourt.org/')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "special"})
# notification = table.find('div', string = re.compile('02/25/22'))
# print(notification)

#Butte County
# r = requests.get('https://www.buttecourt.ca.gov/PressInfo/')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': 'w3-card-2 w3-padding'})
# notification = table.find('p', string = re.compile('November 15, 2021'))
# print(notification)

#Colusa County
# r = requests.get('https://www.colusa.courts.ca.gov/general-information/news')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('April 20, 2021'))
# print(notification)

#Contra Costa County
# r = requests.get('https://www.contracosta.ca.gov/CivicAlerts.aspx?CID=37')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'id': "37"})
# notification = table.find('span', string = re.compile('March 2, 2022'))
# print(notification)

#El Dorado County
# r = requests.get('https://www.eldorado.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('January 27, 2022'))
# print(notification)

#Fresno County
# r = requests.get('https://www.fresno.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('November 22, 2021'))
# print(notification)

#Humboldt County
# r = requests.get('https://www.humboldt.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('February 15, 2022'))
# print(notification)

#Imperial County
# r = requests.get('https://www.imperial.courts.ca.gov/general-information/news-and-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('February 16, 2022'))
# print(notification)

#Inyo County
# r = requests.get('https://www.inyo.courts.ca.gov/views/news')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('June 24, 2021'))
# print(notification)

#Kern County
# r = requests.get('https://www.kern.courts.ca.gov/announcements')
# soup = bs(r.content, features="lxml")
# table = soup.find('body')
# notification = table.find(string = re.compile('18 Feb 2022'))
# print(notification)

#Kings County
# r = requests.get('https://www.kings.courts.ca.gov/views/news')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('April 23, 2021'))
# print(notification)

#Lake County
# r = requests.get('https://www.lake.courts.ca.gov/index.htm')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "contentLeftHomeColumn col-xs-3"})
# notification = table.find(string = re.compile('April 23, 2021'))
# print(notification)

#Lassen County
# r = requests.get('https://www.lassencourt.ca.gov/')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "bgThreeColumn"})
# notification = table.find(string = re.compile('October 25, 2021'))
# print(notification)

#LA County Attorney Notice
# r = requests.get('https://www.lacourt.org/newsmedia/notices/attorneynotice')
# soup = bs(r.content, features="lxml")
# headers = soup.find_all('tbody')
# table = soup.find('table', attrs={'id': "siteMasterHolder_generalInfoLeftHolder_ctl00_tblAll"})
# notification = table.find(string = re.compile("03/01/2022"))
# print(notification)

# #LA County Public Notice
# r = requests.get('https://www.lacourt.org/newsmedia/notices/publicnotices')
# soup = bs(r.content, features="lxml")
# headers = soup.find_all('tbody')
# table = soup.find('table', attrs={'id': "siteMasterHolder_generalInfoLeftHolder_ctl00_tblAll"})
# notification = table.find(string = re.compile("02/08/2022"))
# print(notification)

#Madera County
# r = requests.get('https://www.madera.courts.ca.gov/views/news')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('March 02, 2022'))
# print(notification)

#Marin County
# r = requests.get('http://www.marincourt.org/home.cgi')
# soup = bs(r.content, features="lxml")
# table = soup.find('table', attrs={'width': "270px"})
# notification = table.find(string = re.compile('2/27/2022'))
# print(notification)

#Mariposa County
# r = requests.get('https://www.mariposa.courts.ca.gov/general-information/news-and-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('March 01, 2022'))
# print(notification)

#Mendocino County
# r = requests.get('https://www.mendocino.courts.ca.gov/general-information/court-rules-orders')
# soup = bs(r.content, features="lxml")
# table = soup.find('main', attrs = {'id': 'main-content'})
# notification = table.find(string = re.compile('January 4, 2022'))
# print(notification)

#Merced County
# r = requests.get('https://www.merced.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('January 31, 2022'))
# print(notification)

#Modoc County
# r = requests.get('https://www.modoc.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('October 21, 2021'))
# print(notification)

#Mono County
# r = requests.get('https://www.mono.courts.ca.gov/general-information/news-and-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('July 30, 2021'))
# print(notification)

#Monterey County News
# r = requests.get('https://www.monterey.courts.ca.gov/news')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "jumbotron white"})
# notification = table.find(string = re.compile('January 5, 2022'))
# print(notification)

#Monterey County Homepage
# r = requests.get('https://www.monterey.courts.ca.gov/')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "col-lg-12 col-xl-12"})
# notification = table.find(string = re.compile('February 15, 2022'))
# print(notification)

#Napa County
# r = requests.get('https://www.napa.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('December 16, 2021'))
# print(notification)

#Nevada County
# r = requests.get('http://nccourt.net/index.shtml')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "contentCenter"})
# notification = table.find(string = re.compile('March 3, 2022'))
# print(notification)

