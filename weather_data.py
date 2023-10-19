from requests_html import HTMLSession

s = HTMLSession()
query = input('Enter City: ')
url = f'https://search.yahoo.com/search?fr=mcafee&type=E210US739G0&p=weather+{query}'


r = s.get(url,headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'})

city = r.html.find('h3.fz-20.lh-26',first=True).text
weather = r.html.find('div.imperial-metric',first=True).attrs['data-metric']
cel = r.html.find('button[aria-label="Set units to Celsius"]',first=True).text
details = r.html.find('p.fz-14.lh-20.fc-charcoal.pt-1',first=True).text 
print(city,weather,cel,details)
