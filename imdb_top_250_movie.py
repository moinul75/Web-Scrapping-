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
        rel_year = re.search(r'\b\d{4}\b', rel.text)
        durations = re.findall(r'\b\d{1,2}h \d{1,2}m\b', rel.text)
        ratings = re.findall(r'\b(?:PG-13|R|G|Not Rated|18\+|Approved)\b', rel.text, re.IGNORECASE)
        for rating in ratings:
            rating_movie = rating

        if durations:
            for length in durations:
                movie_length = length

        if rel_year:
            release_year = rel_year.group()
    vote_count = soup.find_all('span',class_='ipc-rating-star--voteCount')
    for vote in vote_count:
        vote_text = vote.get_text(strip=True)
        vote_text = vote_text.replace("(", "").replace(")", "")
        #print(vote_text)

    rating_spans = soup.find_all('span', class_='ipc-rating-star--imdb')

    if rating_spans:
        for rate_span in rating_spans:
            rates = rate_span.get_text(strip=True)
            r = re.search(r'([\d.]+)',rates)
            rate = r.group(1)
           # print(rate)
    
    #now store this on a ecel file 

        

   
except Exception as e: 
    print(e)
