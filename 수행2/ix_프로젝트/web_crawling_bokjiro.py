from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "https://www.bokjiro.go.kr/nwel/welfareinfo/mywelsrv/WelSvcAplPsblt.do"
    data = {"searchIntClId" : "03" , "pageUnit" : "100"}
    with requests.post(url,data) as response:
        soup = BeautifulSoup(response.text, 'lxml')
    print(soup)

    titles = soup.select("dt.tit > a") #<dt class = :title"><a></a></dt>
    for title in titles:
        print(title.text)