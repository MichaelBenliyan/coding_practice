import string
import requests
from bs4 import BeautifulSoup as bs
import re


# Alameda County
# r = requests.get('http://www.alameda.courts.ca.gov/Default.aspx')
# soup = bs(r.content, features="lxml")
# table = soup.find('td', attrs={'class':'bulletLinks'})
# notification = table.find('strong', string = re.compile('2/14/22'))
# print(notification)

# Alpine County
# r = requests.get('https://www.alpine.courts.ca.gov/views/news')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('October 14, 2021'))
# print(notification)

# Amador County
# r = requests.get('https://www.amadorcourt.org/')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "special"})
# notification = table.find('div', string = re.compile('02/25/22'))
# print(notification)

# Butte County
# r = requests.get('https://www.buttecourt.ca.gov/PressInfo/')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': 'w3-card-2 w3-padding'})
# notification = table.find('p', string = re.compile('November 15, 2021'))
# print(notification)

# Colusa County
# r = requests.get('https://www.colusa.courts.ca.gov/general-information/news')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('April 20, 2021'))
# print(notification)

# Contra Costa County
# r = requests.get('https://www.contracosta.ca.gov/CivicAlerts.aspx?CID=37')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'id': "37"})
# notification = table.find('span', string = re.compile('March 2, 2022'))
# print(notification)

# El Dorado County
# r = requests.get('https://www.eldorado.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('January 27, 2022'))
# print(notification)

# Fresno County
# r = requests.get('https://www.fresno.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('November 22, 2021'))
# print(notification)

# Humboldt County
# r = requests.get('https://www.humboldt.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('February 15, 2022'))
# print(notification)

# Imperial County
# r = requests.get('https://www.imperial.courts.ca.gov/general-information/news-and-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('February 16, 2022'))
# print(notification)

# Inyo County
# r = requests.get('https://www.inyo.courts.ca.gov/views/news')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('June 24, 2021'))
# print(notification)

# Kern County
# r = requests.get('https://www.kern.courts.ca.gov/announcements')
# soup = bs(r.content, features="lxml")
# table = soup.find('body')
# notification = table.find(string = re.compile('18 Feb 2022'))
# print(notification)

# Kings County
# r = requests.get('https://www.kings.courts.ca.gov/views/news')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find('div', string = re.compile('April 23, 2021'))
# print(notification)

# Lake County
# r = requests.get('https://www.lake.courts.ca.gov/index.htm')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "contentLeftHomeColumn col-xs-3"})
# notification = table.find(string = re.compile('April 23, 2021'))
# print(notification)

# Lassen County
# r = requests.get('https://www.lassencourt.ca.gov/')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "bgThreeColumn"})
# notification = table.find(string = re.compile('October 25, 2021'))
# print(notification)

# LA County Attorney Notice
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

# Madera County
# r = requests.get('https://www.madera.courts.ca.gov/views/news')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('March 02, 2022'))
# print(notification)

# Marin County
# r = requests.get('http://www.marincourt.org/home.cgi')
# soup = bs(r.content, features="lxml")
# table = soup.find('table', attrs={'width': "270px"})
# notification = table.find(string = re.compile('2/27/2022'))
# print(notification)

# Mariposa County
# r = requests.get('https://www.mariposa.courts.ca.gov/general-information/news-and-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('March 01, 2022'))
# print(notification)

# Mendocino County
# r = requests.get('https://www.mendocino.courts.ca.gov/general-information/court-rules-orders')
# soup = bs(r.content, features="lxml")
# table = soup.find('main', attrs = {'id': 'main-content'})
# notification = table.find(string = re.compile('January 4, 2022'))
# print(notification)

# Merced County
# r = requests.get('https://www.merced.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('January 31, 2022'))
# print(notification)

# Modoc County
# r = requests.get('https://www.modoc.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('October 21, 2021'))
# print(notification)

# Mono County
# r = requests.get('https://www.mono.courts.ca.gov/general-information/news-and-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('July 30, 2021'))
# print(notification)

# Monterey County News
# r = requests.get('https://www.monterey.courts.ca.gov/news')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "jumbotron white"})
# notification = table.find(string = re.compile('January 5, 2022'))
# print(notification)

# Monterey County Homepage
# r = requests.get('https://www.monterey.courts.ca.gov/')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "col-lg-12 col-xl-12"})
# notification = table.find(string = re.compile('February 15, 2022'))
# print(notification)

# Napa County
# r = requests.get('https://www.napa.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('December 16, 2021'))
# print(notification)

# Nevada County
# r = requests.get('http://nccourt.net/index.shtml')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "contentCenter"})
# notification = table.find(string = re.compile('March 3, 2022'))
# print(notification)

# Riverside County Homepage
# r = requests.get('https://riverside.courts.ca.gov/GeneralInfo/MediaInfo/notices.php')
# soup = bs(r.content, features="lxml")
# table = soup.find('table', attrs={'class': "basic-table"})
# notification = table.find(string = re.compile('02/22/2022'))
# print(notification)

# Riverside County Covid
# r = requests.get('https://riverside.courts.ca.gov/PublicNotices/COVID-19-Court-Operations.php')
# soup = bs(r.content, features="lxml")
# table = soup.find('table', attrs={'id': "orders-table"})
# notification = table.find(string = re.compile('02/21/2022'))
# print(notification)

# Sacramento County 
# r = requests.get('https://www.saccourt.ca.gov/general/news-releases.aspx')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "row page-row"})
# notification = table.find(string = re.compile('02.25.22'))
# print(notification)

# San Benito County
# r = requests.get('https://www.sanbenito.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('February 18, 2022'))
# print(notification)

# San Bernardino County
# r = requests.get('https://www.sb-court.org/news-notice')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "views-element-container form-group"})
# notification = table.find(string = re.compile('Mar 03, 2022'))
# print(notification)

# San Diego County
# r = requests.get('https://www.sdcourt.ca.gov/news-release')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "views-element-container"})
# notification = table.find(string = re.compile('March 3, 2022'))
# print(notification)

# San Luis Obispo County
# r = requests.get('https://www.slo.courts.ca.gov/general-information/news-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('March 01, 2022'))
# print(notification)

# Santa Barbara County
# r = requests.get('https://www.sbcourts.org/')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "simpleModule3"})
# notification = table.find(string = re.compile('October 14, 2021'))
# print(notification)

# Santa Clara County Main News
# r = requests.get('https://www.scscourt.org/general_info/news_media/policy_publicntc_news.shtml')
# soup = bs(r.content, features="lxml")
# table = soup.find('body')
# notification = table.find(string = re.compile('March 3, 2022'))
# print(notification)

# Santa Clara County Temp News
# r = requests.get('https://www.scscourt.org/general_info/news_media/tempnews.shtml')
# soup = bs(r.content, features="lxml")
# table = soup.find('body')
# notification = table.find(string = re.compile('February 23, 2022'))
# print(notification)

# Santa Cruz County
# r = requests.get('https://www.santacruz.courts.ca.gov/general-information/news-and-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('February 25, 2022'))
# print(notification)

# Sierra County
# r = requests.get('https://www.sierra.courts.ca.gov/general-information/news-and-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('March 02, 2022'))
# print(notification)

# Siskiyou County
# r = requests.get('https://www.siskiyou.courts.ca.gov/general-information/news-and-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('March 01, 2022'))
# print(notification)

# Solano County
# r = requests.get('https://solano.courts.ca.gov/administration/press-releases-public-notices/')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "col-lg-12"})
# notification = table.find(string = re.compile('February 9, 2022'))
# print(notification)

# Stanislaus County
# r = requests.get('https://www.stanct.org/')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "contentColumn"})
# notification = table.find(string = re.compile('February 1, 2022'))
# print(notification)

# Sutter County
# r = requests.get('https://www.sutter.courts.ca.gov/general-information/news-and-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('July 09, 2021'))
# print(notification)

# Tehama County
# r = requests.get('https://www.tehama.courts.ca.gov/general-information/news-and-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('January 03, 2022'))
# print(notification)

# Tulare County
# r = requests.get('https://www.tulare.courts.ca.gov/general-information/news')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('December 03, 2021'))
# print(notification)

# Ventura County
# r = requests.get('http://www.ventura.courts.ca.gov/public-notice.html')
# soup = bs(r.content, features="lxml")
# table = soup.find('div', attrs={'class': "simpleModuleX"})
# notification = table.find(string = re.compile('January 3, 2022'))
# print(notification)

# Yolo County
# r = requests.get('https://www.yolo.courts.ca.gov/general-information/local-rules-news-notices-orders-and-policies')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('Mar 02, 2022'))
# print(notification)

# Yuba County
# r = requests.get('https://www.yuba.courts.ca.gov/general-information/news-and-events')
# soup = bs(r.content, features="lxml")
# table = soup.find('ul', attrs={'class': "jcc-news-listing__items"})
# notification = table.find(string = re.compile('January 04, 2022'))
# print(notification)




