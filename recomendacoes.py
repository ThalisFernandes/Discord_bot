import requests
import time
from bs4 import BeautifulSoup as Bs


data = requests.get('https://www.youtube.com')
data = Bs(data.content, 'html.parser')
for a in data.find_all('a'):
    print(a)