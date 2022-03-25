import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from flask import Flask, render_template
from io import BytesIO
import base64
import pandas as pd
import numpy as np

app = Flask(__name__)

# Index Route and Function
@app.route('/')
def home():
   return render_template('scrapped_data.html', plot_url=graphs(), symbols=getSymbols()[1], sysIndex=getSymbols()[2])

@app.route('/test/')
def test():
   return "Hi mom"

# All graphs
@app.route('/graphs/')
def graphs():
   img = BytesIO()

   money = getSymbols()[0]
   symbol = getSymbols()[1]

   # row,columns,index
   plt.subplots(figsize=(12, 16))
   plt.subplot(4,1,1)
   plt.bar(symbol, money)
   plt.title('Bar Graph')

   plt.subplot(4,1,2)
   plt.plot(symbol, money)
   plt.title('Plot Graph')

   plt.subplot(4,1,3)
   plt.pie(money, labels=symbol, autopct='%1.1f%%')
   # plt.legend(symbol)
   plt.title('Pie Chart')

   plt.subplot(4,1,4)
   plt.scatter(symbol, money)
   plt.title('Scatter Plot')

   # fig, ax = plt.subplots(figsize=(10, 6))
   # plt.xlabel("Date")
   # plt.ylabel("New Cases")
   # data['Last Price'].plot(ax=ax[0],marker='o')
   # data['Last Price'].plot(kind='bar',ax=ax[1])
   # plt.suptitle(" stocks last price ")

   plt.savefig(img, format='png')
   plt.close()
   img.seek(0)

   return base64.b64encode(img.getvalue()).decode('utf8')


# Get Symbols
def getSymbols():
   sys = pd.read_csv('scrapped_stock_data.csv')
   data = sys['Symbol'].head(15)
   money = sys['Last Price'].head(15)
   listed = [list(money), list(data), [x for x in range(0,30)]]
   return listed


# Selected Symbol
@app.route('/symbol/<string:symbol>')
def symbols(symbol):
   print(symbol)
      # data = pd.read_csv('scrapped_stock_data.csv')
      # data = data[symbol]

   # fig, axes = plt.subplots(nrows=1,ncols=2, figsize=(12, 4) )
   # data.plot(ax=axes[0],marker='o')
   # data.plot(kind='bar',ax=axes[1])
   # plt.suptitle("Bank Statement Graphs")
   # plt.savefig(img, format='png')
   # plt.close()
   # img.seek(0)
   # return base64.b64encode(img.getvalue()).decode('utf8')

   return symbol

if __name__ == '__main__':
   app.run(debug = True)
