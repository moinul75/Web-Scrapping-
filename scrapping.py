#import all the library 
from bs4 import BeautifulSoup 
import requests


#get the url 
url = 'https://www.pararius.com/apartments/amsterdam?ac=1'
#get the page 
page = requests.get(url)


#get the lists of data
soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('section',class_="listing-search-item")
print(lists)


for list in lists:
    title = list.find('a',class_='listing-search-item__link listing-search-item__link--title').text
    location = list.find('div',class_='listing-search-item__sub-title').text
    price = list.find('div',class_="listing-search-item__price").text
    area = list.find('li',class_="illustrated-features__item illustrated-features__item--surface-area").text
    info = [title,location,price,area]
    print(info)
    
