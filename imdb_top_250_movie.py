import requests 
from bs4 import BeautifulSoup 
import re 
import pandas as pd
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


    #store the data 
    movies_names_data = []
    movie_rating_data = []
    movie_vote_data = []
    movie_release_data = []
    movie_duration_data = []
    movie_rate_grade = []
  
    #for title scrap 
    title = soup.find_all('h3',class_='ipc-title__text')
    for t in title[1:251]: 
        tle = t.text.split('. ',1)
        if len(tle) > 1 : 
            movie_title = tle[1]
           # print(movie_title)
            movies_names_data.append(movie_title)

    #for release data
    realeases = soup.find_all('div', class_ ='sc-c7e5f54-7 brlapf cli-title-metadata')
    releases = soup.find_all('div', class_='sc-c7e5f54-7 brlapf cli-title-metadata')
    length = len(releases)
    # print("Number of elements in releases:", length)
    for release in releases:
        metadata_items = release.find_all('span', class_='sc-c7e5f54-8 hgjcbi cli-title-metadata-item')

        if len(metadata_items) == 3:
            release_date = metadata_items[0]
            duration = metadata_items[1]
            grade = metadata_items[2]

            for i in release_date: 
                movie_release_data.append(i.text)
            for i in duration: 
                movie_duration_data.append(i.text)
            for i in grade: 
                movie_rate_grade.append(i.text)

            # Now you can use these variables as needed
            # print("Release Date:", release_date)
            # print("Duration:", duration)
            # print("Grade:", grade)
        else:
            print("The HTML structure has changed or is not as expected.")
    # for rel in realeases:
    #     rel_year = re.search(r'\b\d{4}\b', rel.text)
    #     durations = re.findall(r'\b(?:\d+h\s*)?\d+m\b', rel.text)
    #     ratings = re.findall(r'\b(?:PG-13|R|G|Not Rated|Approved|Passed|16\+|18\+)\b', rel.text)
    #     if ratings:
    #         for rating in ratings:
    #             rating_movie = rating
    #             movie_rate_grade.append(rating_movie)

    #     if durations:
    #         for length in durations:
    #             movie_length = length
    #             movie_duration_data.append(movie_length)
    #             # Filling in "N/A" for missing ratings

  

    
    #     if rel_year:
    #         release_year = rel_year.group()
    #         movie_release_data.append(release_year)

    vote_count = soup.find_all('span',class_='ipc-rating-star--voteCount')
    for vote in vote_count:
        vote_text = vote.get_text(strip=True)
        vote_text = vote_text.replace("(", "").replace(")", "")
        movie_vote_data.append(vote_text)

    rating_spans = soup.find_all('span', class_='ipc-rating-star--imdb')

    if rating_spans:
        for rate_span in rating_spans:
            rates = rate_span.get_text(strip=True)
            r = re.search(r'([\d.]+)',rates)
            rate = r.group(1)
            movie_rating_data.append(rate)
    
    #now store this on a ecel file 
    data = {
        'Name':movies_names_data,
        'Duration': movie_duration_data,
        'Release_Date': movie_release_data,
        'Rating': movie_rating_data,
        'Grade': movie_rate_grade,
        'Vote': movie_vote_data
        #
    }
    print(len(movie_rate_grade))
    print(len(movie_vote_data))
    print(len(movie_duration_data))
    print(len(movies_names_data))
    print(len(movie_release_data))
    print(len(movie_rating_data))

    # Find the maximum column length
    max_len = max(len(data['Name']), len(data['Duration']), len(data['Release_Date']), len(data['Rating']), len(data['Grade']), len(data['Vote']))

    # Pad shorter columns with "N/A" to match the maximum length
    for key in data.keys():
        data[key] = data[key] + ["N/A"] * (max_len - len(data[key]))

    # Create a DataFrame
    df = pd.DataFrame(data, columns=['Name', 'Duration', 'Release_Date', 'Rating', 'Grade', 'Vote'])

    # Save the DataFrame to an Excel file
    df.to_excel('imdb_top_250_movie.xlsx', header=False, index=False)

   
except Exception as e: 
    print(e)
