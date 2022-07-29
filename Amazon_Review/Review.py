
import requests
from bs4 import BeautifulSoup
import pandas as pd




class Amazon:

    def __init__(self):
        self.reviewlist = []

    def __get_soup(self,url):
        r = requests.get(url, params={'wait':2})

        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    def __get_review(self,soup):
        reviews = soup.find_all('div', {'data-hook':'review'})

        try:
            for item in reviews:
                review = {
                'product': soup.title.text.replace('Amazon.in:Customer reviews:', '').strip(),
                'title' : item.find('a', {'data-hook': 'review-title'}).text.strip(),
                'rating' : float(item.find('i', {'data-hook':'review-star-rating'}).text.replace('out of 5 stars','').strip()),
                'body' : item.find('span', {'data-hook':'review-body'}).text.strip()
                }
                self.reviewlist.append(review)
        except:
            pass

    def get_data(self, pageNumber):
        for x in range(1,pageNumber):
            url = f'https://www.amazon.in/New-Apple-iPhone-12-128GB/product-reviews/B08L5WD9D6/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}'   
            soup = self.__get_soup(url)
            self.__get_review(soup)
            
            if not soup.find('li', {'class':'a-disabled a-last'}):
                pass
            else:
                break
        df = pd.DataFrame(self.reviewlist)
        df.to_csv("Amazon_Review.csv")

A = Amazon()
A.get_data(3)



