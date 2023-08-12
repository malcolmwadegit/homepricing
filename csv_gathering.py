## Data visualiztion Examples
import requests
import pandas as pd  
from bs4 import BeautifulSoup



def csv_gathering_price():
    req = requests.get("https://data.nasdaq.com/tables/ZILLOW/ZILLOW-DATA/export")
    url_content = req.content
    csv_file = open('price_downloaded.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()

def csv_gathering_location():
    req = requests.get("https://data.nasdaq.com/tables/ZILLOW/ZILLOW-REGIONS/export")
    url_content = req.content
    csv_file = open('location_downloaded.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()

    
def csv_reader():
    data = pd.read_csv('')
    query_data = data.query('')
    column_select = query_data[[]]
    print(column_select)
    




csv_gathering_price()
csv_gathering_location()