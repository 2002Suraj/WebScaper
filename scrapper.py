import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
#print(r)

soup = BeautifulSoup(r.text, 'lxml')
#print(soup)

table = soup.find("table",class_="ih-td-tab auction-tbl")
#print(table)

title = table.find_all("th")
# print(title)
header=[]
for i in title :
    name = i.text
    header.append(name)
df = pd.DataFrame(columns=header)
#print(df)


rows = table.find_all("tr")
#print(row)

for i in rows[1:]:
    td_elements = i.find_all("td")
    if td_elements:
        first_td = td_elements[0].find("div", class_= "ih-pt-ic")
        if first_td:
            first_td_text = first_td.get_text(strip=True)
            data = td_elements[1:]
            row = [tr.get_text(strip=True) for tr in data]
            row.insert(0, first_td_text)
            df.loc[len(df)] = row
print(df)

df.to_csv("ipl Auction.csv")