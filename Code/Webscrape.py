import requests
import csv
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

book_containers = soup.find_all('article', class_='product_pod')

with open('books.csv', 'w', newline='', encoding='utf-8') as csv_file:

    writer = csv.writer(csv_file)

    writer.writerow(['Title', 'Price', 'Link'])

    for container in book_containers:
        title = container.h3.a.text
        price = container.find('div', class_='product_price').p.text
        link = container.h3.a['href'] 
        writer.writerow([title, price, link])
