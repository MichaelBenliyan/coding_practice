from datetime import datetime
from pytest import skip #date format cheat sheet: https://strftime.org/
import xlrd #excel cheat sheet: https://www.geeksforgeeks.org/reading-excel-file-using-python/
import string
import requests
from bs4 import BeautifulSoup as bs
import re

# datetime.today().strftime('%Y-%m-%d')
date_formats = {} #{1: '%Y-%m-%d'} <- inacurate example
new_notifications = []
row = 1
wb = xlrd.open_workbook("county_list.xls")
sheet = wb.sheet_by_index(0)
while row < 54: 
    if sheet.cell_value(row, 0) == "SKIP": 
        pass
    else:
        site = requests.get(sheet.cell_value(row, 0))
        if sheet.cell_value(row, 1) == 1: 
            pass
        elif sheet.cell_value(row, 1) == 2:
            soup = bs(site.content, features="lxml")
            table = soup.find('td', attrs={'class':'bulletLinks'})
            notification = table.find('strong', string = re.compile(datetime.today().strftime(date_formats[sheet.cell_value(row, 2)])))
        elif sheet.cell_value(row, 1) == 3:
            pass
        elif sheet.cell_value(row, 1) == 4:
            pass
        elif sheet.cell_value(row, 1) == 5:
            pass
        elif sheet.cell_value(row, 1) == 6:
            pass
        elif sheet.cell_value(row, 1) == 7:
            pass
        elif sheet.cell_value(row, 1) == 8:
            pass
        elif sheet.cell_value(row, 1) == 9:
            pass
        elif sheet.cell_value(row, 1) == 10:
            pass
        elif sheet.cell_value(row, 1) == 11:
            pass
        elif sheet.cell_value(row, 1) == 12:
            pass
        elif sheet.cell_value(row, 1) == 13:
            pass
        elif sheet.cell_value(row, 1) == 14:
            pass
        elif sheet.cell_value(row, 1) == 15:
            pass
        elif sheet.cell_value(row, 1) == 16:
            pass
        elif sheet.cell_value(row, 1) == 17:
            pass
        elif sheet.cell_value(row, 1) == 18:
            pass
        elif sheet.cell_value(row, 1) == 19:
            pass
        elif sheet.cell_value(row, 1) == 20:
            pass
        elif sheet.cell_value(row, 1) == 21:
            pass
        elif sheet.cell_value(row, 1) == 22:
            pass
        elif sheet.cell_value(row, 1) == 23:
            pass
        if notification != None: 
            new_notifications.append(sheet.cell_value(row, 3))
    row += 1
print(new_notifications)