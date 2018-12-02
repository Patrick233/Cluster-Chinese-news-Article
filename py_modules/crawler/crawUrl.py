from bs4 import BeautifulSoup
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def download(title, url, m):
    # req = request.Request(url)
    # print (url)
    response = requests.get(url)
    response.encoding = 'utf-8'
    print (response.status_code)
    soup = BeautifulSoup(response.text, 'lxml')
    tags = soup.find_all('p')
    str = ""
    for tag in tags[:-1]:
        # tag = tags
        str += tag.get_text()
        # print (tag.get_text())
        if tag == None:
            continue

    filename = r'/Users/Patrizio/Desktop/neu/cs6220/project/news/education/' + title + '.txt'

    try:
        with open(filename, 'w') as file_object:
            content = str
            # content = content.encode('ascii', 'ignore').decode('ascii')
            # print (content)
            file_object.write(content)
            file_object.close()
    except Exception, e:
        print (e)
        print ("This is not right")
    print('Crawling', m, ' news:', title)
    return 0

def findCat():
    lst = ['ent', 'sports', 'tech', 'edu', 'health', 'fashion']
    # base_url = 'https://interface.sina.cn/ent/feed.d.json?ch={}&col=ent&act=more&show_num=100&page={}&isLongTitle=true'
    url = 'https://interface.sina.cn/ent/feed.d.json?ch=edu&col=ent&act=more&show_num=100&page={}&isLongTitle=true'
    print (url)
    s = set()
    for i in range(54,100):
        page = url.format(i)
        y = 0
        print (page)
        # print ("Crawling page {}".format(url))
        print ("Number: {}".format(y))

        response = requests.get(page)
        json = response.json()

        data = json["data"]
        print (data)

        for news in data:
            download(news["title"], news["link"], y)
            print ("Title: {}".format(news["title"]))
            s.add(news["title"])
            y = y + 1

        # print(news)
    print "Size is :{}".format(len(s))

if __name__ == '__main__':
    # url = 'https://ent.sina.cn/film/foreign/2018-11-08/detail-ihnprhzw4257001.d.html'
    # tag = "test"
    # y = 0
    # download(tag, url, 0)
    findCat()

