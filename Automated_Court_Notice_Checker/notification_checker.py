from datetime import datetime
from datetime import timedelta
from pytest import skip #date format cheat sheet: https://strftime.org/
import xlrd 
import string
import requests
from bs4 import BeautifulSoup as bs
import re

today = datetime.today()
yesterday = today - timedelta(days = 1)
date_formats = {
    1.0: '%-m/%-d/%y',
    2.0: '%B %d, %Y',
    3.0: '%m/%d/%y',
    4.0: '%B %-d, %Y',
    5.0: '%m/%d/%Y',
    6.0: '%-d %b %Y',
    7.0: '%-m/%-d/%Y',
    8.0: '%m.%d.%y',
    9.0: '%b %d, %Y'
}
search_format = {
    1.0: {'tag': 'ul', 'attrs_tag': "class", 'attrs_title': 'jcc-news-listing__items'}, 
    2.0: {'tag': 'td', 'attrs_tag': "class", 'attrs_title': 'bulletLinks'}, 
    3.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'special'},
    4.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'w3-card-2 w3-padding'},
    5.0: {'tag': 'div', 'attrs_tag': 'id', 'attrs_title': '37'},
    6.0: {'tag': 'body'},
    7.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'contentLeftHomeColumn col-xs-3'},
    8.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'bgThreeColumn'},
    9.0: {'tag': 'table', 'attrs_tag': 'id', 'attrs_title': 'siteMasterHolder_generalInfoLeftHolder_ctl00_tblAll'},
    10.0: {'tag': 'table', 'attrs_tag': 'width', 'attrs_title': '270px'},
    11.0: {'tag': 'main', 'attrs_tag': 'id', 'attrs_title': 'main-content'},
    12.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'jumbotron white'},
    13.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'col-lg-12 col-xl-12'},
    14.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'contentCenter'},
    15.0: {'tag': 'table', 'attrs_tag': 'class', 'attrs_title': 'basic-table'},
    16.0: {'tag': 'table', 'attrs_tag': 'id', 'attrs_title': 'orders-table'},
    17.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'row page-row'},
    18.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'views-element-container form-group'},
    19.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'views-element-container'},
    20.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'simpleModule3'},
    21.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'col-lg-12'},
    22.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'contentColumn'},
    23.0: {'tag': 'div', 'attrs_tag': 'class', 'attrs_title': 'simpleModuleX'},    
} 
new_notifications = []
row = 1
wb = xlrd.open_workbook("county_list.xls")
sheet = wb.sheet_by_index(0)
while row < 54: 
    if sheet.cell_value(row, 0) == "SKIP": 
        pass
    else:
        site = requests.get(sheet.cell_value(row, 0))
        soup = bs(site.content, features="lxml")
        if "attrs_tag" in search_format[sheet.cell_value(row, 1)]:
            table = soup.find(search_format[sheet.cell_value(row, 1)]['tag'], attrs={search_format[sheet.cell_value(row, 1)]['attrs_tag']: search_format[sheet.cell_value(row, 1)]['attrs_title']})
        else: 
            table = soup.find(search_format[sheet.cell_value(row, 1)]['tag'])
        notification = table.find(string = re.compile(today.strftime(date_formats[sheet.cell_value(row, 2)])))
        if notification != None: 
            new_notifications.append(sheet.cell_value(row, 3))
    row += 1
print(new_notifications)