
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# put the url from the PDF
#bright_stars_url = 

page = requests.get(bright_stars_url)
#print(page)

soup = bs(page.text,'html.parser')
# use soup.find() by passing 'table' as parameter and assign to variable star_table

# take an empty list vaiable called temp_list

#use star_table.find_all('tr') and assign to table_rows

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)



Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])
    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)

#use df2.to_csv and pass a file name 
