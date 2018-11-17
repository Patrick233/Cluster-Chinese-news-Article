from bs4 import BeautifulSoup
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def download(title, url, m):
    # req = request.Request(url)
    # print (url)
    response = requests.get(url)
    #  response = response.read().decode('utf-8')
    response.encoding = 'utf-8'
    print (response.status_code)
    soup = BeautifulSoup(response.text, 'lxml')
    tag = soup.find('div', class_='article')
    if tag == None:
        return 0
    # print(type(tag))
    # print(tag.get_text())
    title = title.replace(':', '')
    title = title.replace('"', '')
    title = title.replace('|', '')
    title = title.replace('/', '')
    title = title.replace('\\', '')
    title = title.replace('*', '')
    title = title.replace('<', '')
    title = title.replace('>', '')
    title = title.replace('?', '')
    filename = r'/Users/Patrizio/Desktop/neu/cs6220/project/Soccer/' + title + '.txt'

    try:
        with open(filename, 'w') as file_object:
            file_object.write('           ')
            file_object.write(title)
            content = tag.get_text()
            # content = content.encode('ascii', 'ignore').decode('ascii')
            print (content)
            file_object.write(content)
            file_object.close()
    except Exception, e:
        print (e)
        print ("This is not right")
    print('Crawling', m, ' news:', title)
    return 0


if __name__ == '__main__':
    target_url = 'http://interface.sina.cn/pc_zt_roll_news_index.d.html?vt=4&subjectID=64558&channel=sports'
    response = requests.get(target_url)
    response.encoding = 'utf-8'
    # print(response.status_code)
    soup = BeautifulSoup(response.text, 'lxml')
    # print (soup)
    # print(soup.prettify())
    # file = open('d:\\test2.txt','w',encoding='utf8')
    # file.write(soup.prettify())
    y = 0
    # for tag in soup.find_all('div',class_='vBody'):
    body = soup.select("div  ul")
    # body = soup.find('body').find("div", {"id":"vbody"})
    print (body)
    children = body.find_all("li", recursive=False)

    for tag in body:
        print (tag)
        if tag.a != None:
            # print (tag)
            try:
                if len(tag.a.string) > 8:
                    # print(tag.a.string,tag.a.get('href'))
                    temp = tag.a.string
                    y += 1
                    download(temp, tag.a.get('href'), y)
            except Exception, e:
                print (e.message)
                print("Some thing's wrong")
