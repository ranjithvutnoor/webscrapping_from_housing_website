from bs4 import BeautifulSoup
import requests
import csv
from csv import writer


url='https://www.pararius.com/apartments/amsterdam'
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
jobs = soup.find_all('section',class_='listing-search-item')

with open('housing.csv','w',encoding='utf8',newline='') as f:
    thewriter= writer(f)
    header=['title','location','price','area','rooms','interior']
    thewriter.writerow(header)

    for job in jobs:
        title = job.find('h2',class_='listing-search-item__title').text.replace('\n','').strip()
        location = job.find('div', class_='listing-search-item__location').text.replace('\n','').strip()
        price = job.find('div', class_='listing-search-item__price').text.replace('\n','').strip()
        features = job.find('u1', class_='illustrated-features illustrated-features--compact')
        area = job.find('li',class_='illustrated-features__item illustrated-features__item--surface-area').text.replace('\n','').strip()
        rooms = job.find('li', class_='illustrated-features__item illustrated-features__item--number-of-rooms').text.replace('\n','').strip()
        interior = job.find('li', class_='illustrated-features__item illustrated-features__item--interior').text.replace('\n','').strip()
        info=[title,location,price,area,rooms,interior]
        thewriter.writerow(info)
