#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':

    data = urlopen('https://comic.naver.com/webtoon/list.nhn?titleId=651673&weekday=wed')
    soup = BeautifulSoup(data,'lxml')
    #print(soup)

    cartoon_titles = soup.find_all('td', attrs = {'class' : 'title'}) #td에 class title 속성을 찾음
    for cartoon_titles in cartoon_titles:
        title = cartoon_titles.find('a').text
        link = cartoon_titles.find('a').get("herf") #href 속성 가져오기
        link = 'https://comic.naver.com' + link
        print(title)
        print(link)