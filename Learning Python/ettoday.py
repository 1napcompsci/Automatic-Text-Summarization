# 載入python 套件
import requests
from bs4 import BeautifulSoup  

# https://www.ettoday.net/news/news-list-2017-07-15-5.htm
# 1 政治 
# 17 財經
# 2 國際
# 6 社會
# 9 影劇
# 10 體育
# 20 3c
# 30 時尚 
# 24 遊戲
# 5 生活

# 抓 title
for tt in [1, 17, 2, 6, 9, 10, 20, 30, 24, 5]:
    title = []
    for n in range(1,11):
        for n2 in [25,10]:
            u = "https://www.ettoday.net/news/news-list-2017-"+str(n)+"-"+str(n2)+"-"+str(tt)+".htm"
            res = requests.get(u)
            soup = BeautifulSoup(res.content, "lxml")
            soup = soup.find("div", class_="part_list_2")
            domian = "https://www.ettoday.net"
            for a in soup.find_all("h3"):
                p = a.a.string
                if p != None:
                    p = p.split('／')
                    if len(p) > 1:
                        title.append(p[1])
                    else:
                        title.append(p[0])

    with open(str(tt)+".txt", "a") as f:
        for t in title:
            f. write(t+"\n")
# 抓 內文
for tt in [1, 17, 2, 6, 9, 10, 20, 30, 24, 5]:
    print(tt)
    urls = []
    for n in range(1,11):
        for n2 in [25,10]:
            u = "https://www.ettoday.net/news/news-list-2017-"+str(n)+"-"+str(n2)+"-"+str(tt)+".htm"
            res = requests.get(u)
            soup = BeautifulSoup(res.content, "lxml")
            soup = soup.find("div", class_="part_list_2")
            domian = "https://www.ettoday.net"
            for a in soup.find_all("h3"):
                urls.append(domian+a.a['href'])
    allcontent = []
    for u in urls:
        content = []
        res = requests.get(u)
        soup = BeautifulSoup(res.content, "lxml")
        try:
            soup = soup.find("div", class_="story")
            for a in soup.find_all("p"):
                p = a.string
                if p != None:
                    p = p.split('／')
                    if len(p) > 1:
                        content.append(p[1])
                    else:
                        content.append(p[0])
            allcontent.append(content)
        except:
            pass
    print(len(allcontent))
    with open(str(tt)+".txt", "a") as f:
        for c in allcontent:
            if len(c) > 3:
                ss = ""
                for aaa in c:
                    ss+=aaa+'，'
                f.write(ss+"\n")  