

import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

class IMBD:
    def __init__(self):
        self.Movielist = []
        self.genre_List = ['comdey', 'sci-fi', 'horror', 'romance', 'action', 'thriller'
                           'drama', 'mystery', 'crime', 'animation', 'adventure', 'fantasy', 
                           'superhero']

    def __GetData(self, pageNo, genre):

        url = "https://www.imdb.com/search/title/?genres="+ genre +"&start="
        x = 1
        for i in range(1,pageNo+1):
            u = url + str(x)
            x = x+50
            r = requests.get(u, params={'wait':2})
            soup = BeautifulSoup(r.text, 'html.parser')
            movies = soup.find_all('div', {'class':'lister-item mode-advanced'})
            for movie in movies:
                Movie_list = {
                    'UserId': random.randint(1,50),     
                    'Title' :  movie.find('h3').find('a').text,
                    'Genre' : movie.find('p', {'class':'text-muted'}).find('span', {'class':'genre'}).text,
                    'Rating' : None if movie.find('div', {'class':'ratings-bar'})== None 
                                    else  None if movie.find('div', {'class':'ratings-bar'}).find('strong')==None
                                                   else movie.find('div', {'class':'ratings-bar'}).find('strong').text
                }
                self.Movielist.append(Movie_list)

        df = pd.DataFrame(self.Movielist)
        return df

    def GetMovie(self, pageNo):
        f = []
        for g in self.genre_List:
            data = self.__GetData(pageNo=pageNo, genre=g)
            f.append(data)

        df = pd.concat(f)
        df.to_csv("Movie_Data.csv")
        return df


