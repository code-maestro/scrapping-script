import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create an URL object
url = 'https://finance.yahoo.com/trending-tickers'
# Create object page
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

stocks_table = soup.find('table', class_="W(100%)")

theaders = []
for i in stocks_table.find_all('th'):
    title = i.text
    theaders.append(title)

# lists to store the data
stock_symbol = []
stock_names = []
stock_prices = []

# loop to populate the DataFrame
for j in stocks_table.find_all('tr')[1:]:
    stock_symbol.append(j.find('a', {'class': 'Fw(600)'}).text)
    stock_names.append(j.find('td', {'class': 'Va(m) Ta(start) Px(10px) Miw(180px) Fz(s)'}).text)
    stock_prices.append(j.find('td', {'class': 'Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)'}).text)

# dictionary of lists 
dict = { theaders[0]: stock_symbol, theaders[1]: stock_names, theaders[2]: int(stock_prices)}
df = pd.DataFrame(dict)
df.to_csv('scrapped_stock_data.csv', index=False)

df.plot(kind='bar')

# print(df)












# row_data = j.find_all('td')
# row = [i.text for i in row_data]
# length = len(mydata)
# mydata.loc[length] = row