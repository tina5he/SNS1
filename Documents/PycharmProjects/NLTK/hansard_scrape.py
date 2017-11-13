import numpy as np
import requests
import bs4  as bs
from datascience import *

def get_text(url):
    source = requests.get(url)
    soup = bs.BeautifulSoup(source.content, features='lxml')
    full_text = []
    for p in soup.find_all('p'):
        full_text = np.append(full_text, p.text)
    return " ".join(full_text)

links = Table().read_table('urls.csv')
url = list(set(links.column(0)))
texts =[get_text(i) for i in url]
full_text = Table().with_columns('full_text', texts)
full_text.to_csv('hansards.csv')

