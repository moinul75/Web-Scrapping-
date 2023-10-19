import requests 
from bs4 import BeautifulSoup 
import re 

headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

#so headers is important becaue some website root.txt doesn't allow to scrap any website thats why we need headers which contains browser access to this website html

#tricks 
#if the more then one element is using same class  them for each iteration then use regular expression to separate them 
# use group by to do this  

try: 
    url = 'https://www.imdb.com/chart/top/'
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    #for title scrap 
    title = soup.find_all('h3',class_='ipc-title__text')
    for t in title[1:251]: 
        tle = t.text.split('. ',1)
        if len(tle) > 1 : 
            movie_title = tle[1]
            # print(movie_title)
    #for release data
    realeases = soup.find_all('span', class_ ='sc-c7e5f54-8 hgjcbi cli-title-metadata-item')
    for rel in realeases: 
        rel_year = re.search(r'\b\d{4}\b',rel.text)
        durations = re.findall(r'\b\d{1,2}h \d{1,2}m\b', rel.text)
        rate = re.findall(r'\b[\w-]\b',rel.text)
        print(rate)
        #print(durations)
        if durations: 
            for length in durations: 
                movie_length = length
               # print(movie_length)
        if rel_year: 
            release_year = rel_year.group()
            # print(rel_year) 

    

   
except Exception as e: 
    print(e)
