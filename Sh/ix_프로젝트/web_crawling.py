#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':

    data = urlopen('https://comic.naver.com/webtoon/list.nhn?titleId=651673&weekday=wed')
    soup = BeautifulSoup(data,'lxml')
    data.close()
    #print(soup)

    html = "<html><head><meta charset = 'utf-8'></head><body>"
    cartoon_titles = soup.find_all('td', attrs = {'class' : 'title'}) #td에 class title 속성을 찾음
    for cartoon_titles in cartoon_titles:
        title = cartoon_titles.find('a').text
        link = cartoon_titles.find('a').get("href") #href 속성 가져오기
        link = 'https://comic.naver.com' + link
        print(title)
        print(link)
        html += "<a href = '{}'</a><br/>".format(link,title) #<a href ='link'>title</a>
    html += '</body></html>'
    #print(html)

    outputSoup = BeautifulSoup(html,'lxml')
    prettyHtml = str(outputSoup.prettify())
    with open('유미의 세포들.html', 'w', encoding='utf-8') as f:
        f.write(html)