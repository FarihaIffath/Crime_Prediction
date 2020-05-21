import requests
from bs4 import BeautifulSoup
import pandas as pd


year_list= ['2010','2011','2012','2013','2014','2015','2016','2017','2018']
for year in year_list:
    r = requests.get("https://www.police.gov.bd/en/crime_statistic/year/"+year)

    data =[]
    df=pd.DataFrame()
    
    soup = BeautifulSoup(r.content,"lxml")
    table = soup.select_one("table.table.table-bordered.table-striped.table-hover.table-condensed")
   # print(table)
    
    cols = [th.text for th in table.select("th")[1:]]
    #print(cols)
    table_row = table.find_all('tr')
    #print(table_row)
    for tr in table_row:
        td = tr.find_all('td')
        row = [i.text for i in td]
        print(row)
    col0 = pd.Series(cols)
    df.insert(loc=0,column='Type',value=col0)
    k=1
    for row in table.select("tbody"):
    
        for i in row.select("tr"):
        #data.append(str([td.text for td in i.select("td")]))
            col1 = [td.text for td in i.select("td")]
            x = col1.pop(0)
            col = pd.Series(col1)
            df.insert(loc = k, column=str(x),value=col)
            k=k+1
    #df.to_csv(year+'.csv')
    
        #print(i.text)
    #print(data)
    # use date as the key and store list of values
    
   

    
