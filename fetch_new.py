import requests
from bs4 import BeautifulSoup
import pandas as pd


year_list= ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
for year in year_list:
    r = requests.get("https://www.police.gov.bd/en/crime_statistic/year/"+year)

    data =[]
    df=pd.DataFrame()
    
    soup = BeautifulSoup(r.content,"lxml")
    table = soup.select_one("table.table.table-bordered.table-striped.table-hover.table-condensed")
   # print(table)
    df = pd.read_html(str(table))
    print(df)
    df[0].to_csv(year+'.csv', index=False)
    
