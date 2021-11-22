from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep

# 範例小說網站
# url = 'https://tw.ixdzs.com/read/0/864/p3.html'
url_base = 'https://tw.ixdzs.com/read/0/864/p'
# url_base = 'https://tw.ixdzs.com/read/110/110094/p'


def main(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read())

    # 找content內所有的p tag
    content = bsObj.find(class_='content')
    pars = content.findAll('p')
    # 上面兩行的縮寫版, css selector
    # pars = bsObj.select('div.content p')

    with open('result.txt', 'a') as f:
        for p in pars:
            # 移除預設換行來節省空間
            print(p.get_text(), file=f, end='')
        print(file=f)  # 換行當換頁表示


for i in range(2, 5):
    sleep(3)
    main(url_base+str(i)+'.html')
