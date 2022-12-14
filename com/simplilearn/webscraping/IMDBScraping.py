import requests
from bs4 import BeautifulSoup

try:
    source=requests.get("https://www.imdb.com/chart/top/")
    #status=source.raise_for_status()
    #print(status)
    soup=BeautifulSoup(source.text,'html.parser')
    #print(soup)
    movies=soup.find('tbody', class_="lister-list").find_all('tr')
    #print(movies)

    f = open("IMDB.txt",'a')

    for movie in movies:
        rank=movie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
        #print(rank)
        name=movie.find('td',class_='titleColumn').a.text
        #print(name)
        year=movie.find('td',class_='titleColumn').span.text.strip('()')
        #print(year)
        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
        #print(rating)

        #print(rank,name,year,rating)

        f.write(rank)
        f.write(" ")
        f.write(name)
        f.write(" ")
        f.write(year)
        f.write(" ")
        f.write(rating)
        f.write(" ")
        f.write("\n")
    f.close()




except Exception as e:
    print(e)