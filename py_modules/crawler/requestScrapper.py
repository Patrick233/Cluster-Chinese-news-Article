from bs4 import BeautifulSoup
import requests

url = 'http://news.sina.com.cn/china/'
web_data = requests.get(url)
web_data.encoding = 'utf-8'
soup = BeautifulSoup(web_data.text, 'lxml')
# print (soup)

for news in soup.find_all('div',class_='main-content'):
    print (news)
    if (len(news.select('h2')) > 0):
        h2 = news.select('h2')[0].text
        time = news.select('.time')[0].text
        a = news.select('a')[0]['href']
        print(h2, time, a)
