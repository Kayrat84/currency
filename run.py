from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd
from datetime import date
dt = date.today()
site = rq.get('https://cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01375&UniDbQuery.From=19.01.2021&UniDbQuery.To='+'.'.join(str(dt).split('-')[::-1]))
soup = bs(site.text)
dat = soup.find_all('td')
dct = {dat[i].text: dat[i+2].text for i in range(1, len(dat)-2, 3)}
df = pd.DataFrame(list(dct.items()), columns=['Дата', 'Курс'])
print(df)