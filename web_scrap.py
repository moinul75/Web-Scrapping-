# make a webScrapping with pandas and beautiful soup and re (pricing list )
import requests 
from bs4 import BeautifulSoup 
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

#collections in a list 
names = []
descriptions = []
prices = []
reviews = []
#names 
titles = soup.find_all("a",class_ = "title")
# print(len(titles))
for title in titles: 
    #print(title.text)
    names.append(title.text)

#descriptions 
desc = soup.find_all("p",class_="description card-text")
descriptions = [results.text for results in desc]
# print(descriptions)
#price 
price = soup.find_all("h4",class_ ="float-end price card-title pull-right")
prices = [prc.text for prc in price]
# print(prices) 

#reviews 
review = soup.find_all("p",class_ = "float-end review-count")
reviews = [rev.text for rev in review]
# print(reviews)


#data structure 
data  = {
    'Product_name':names, 
    'Price': prices, 
    'Product_review': reviews
}

#get a DataFrame and make this data frame in a csv format
df = pd.DataFrame(data)

print(df.head())

#csv file 
df.to_csv('price_list.csv',index=False)


