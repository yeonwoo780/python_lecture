import requests
from bs4 import BeautifulSoup
import re

def get_movie_link(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html5lib')
    # print(soup)

    movie_links = soup.select('a[href]')
    # print(movie_links)
    movie_links_list = []
    for link in movie_links: # 네티즌 평점 사이트 default
        if re.search(r'st=mcode&sword' and r'&target=after', link['href']): # 네티즌 평점사이트의 영화제목 10개 받아옴
            target_url = r'http://movie.naver.com/movie/point/af/list.nhn'+str(link['href'])
            movie_links_list.append(target_url)
            # print(movie_links_list)

    return movie_links_list

# url = 'http://movie.naver.com/movie/point/af/list.nhn'
# movie_links = get_movie_link(url)
# print(movie_links)

def genre_list(url):
    movie_links_list = get_movie_link(url) # 앞에서 받아온 10개 제목
    genre_list = []

    for movie_url in movie_links_list: # 앞에서 10개 하나하나씩 들어가서
        res = requests.get(movie_url)
        content = res.text
        soup = BeautifulSoup(content, 'html5lib')
        genre = soup.find_all('table', class_='info_area') # 영화 정보가 있는 테이블 부분 들고와줌

        for genre in genre:
            genre_list.append(genre.a.get_text()) # 그중 장르가 있는 a테그 들고와줌

    return genre_list

# url = 'http://movie.naver.com/movie/point/af/list.nhn'
# genre_list_data = genre_list(url)
# print(genre_list_data)

def get_user_list(url): # 위에서 영화 하나 들고와서 댓글을 쓴 user를 보려고 page10개 들고오는듯?
    res = requests.get(url)
    content = res.text

    soup = BeautifulSoup(content, 'html5lib')

    page_links = soup.select('a[href]')
    page_links_list = []

    for link in page_links:
        if re.search(r'&target=after', link['href']):
            target_url = r'http://movie.naver.com'+str(link['href'])
            page_links_list.append(target_url)

    if len(page_links_list) != 1:
        pop_number = len(page_links_list) - 1
        page_links_list.pop(pop_number)

    return page_links_list

# url = 'https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=187322&target=after'
# point_data = get_user_list(url)
# print(point_data) 
