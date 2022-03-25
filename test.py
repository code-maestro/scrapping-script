import pandas as pd

def getSymbols():
   sys = pd.read_csv('scrapped_stock_data.csv')
   data = sys['Symbol'].head(15)
   money = sys['Last Price'].head(15)

   listed = [list(money), list(data), [x for x in range(0,30)]]
   # listed = [[x for x in range(0, 30)], list(data)]
   return listed

print(getSymbols())

# {% block test %}
# {% for sysI in sysIndex %}
# <li class="overview">
#    <a href="/symbol/{{sysI}}"> {{sysI}} </a>
# </li>
# {% endfor %}
# {% endblock %}