#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

if __name__ == '__main__':

    with urlopen('http://webtoon.daum.net/webtoon/viewer/52250') as data:
        j = json.loads(data.read())
    html = "<html><head><meta charset = 'utf-8'></head><body>"

    cartoon_titles = (j['data']['webtoon']['webtoonEpisoeds'])

    for cartoon_titles in cartoon_titles:
        title = (cartoon_titles['title'])
        print(title)
        thumbnail = cartoon_titles['tumbnailImage'['url']] #http://t1.daumcdn.net/webtoon/op/d1f53ce0342de30c4c5451d070290cbe21edefa6
        print(thumbnail)
        url = cartoon_titles['id']
        url = 'http://t1.daumcdn.net/webtoon/op/d1f53ce0342de30c4c5451d070290cbe21edefa6'+str(url)
        print(url)
    #html += '<a herf ='{}'/><img src = '{}'/></a>'.format()
    html += '</body></html>'



    #print(soup)


