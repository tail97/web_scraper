
#https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu
import requests
from bs4 import BeautifulSoup

# 요청보내기
url = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu'
res = requests.get(url)
# print(res)
# print(res.text)

soup = BeautifulSoup(res.text,"html.parser")
#print(soup)

items = soup.select("tr.list1,tr.list0")

# img_url, title, link, replay_count, up_count을 다 뽑아야한다.
for item in items:
    try:
        img_url = item.select("img.thumb_border")[0].get('src').strip()#strip은 양쪽 공백제거
        #title = item.select("a font.list_title")[0] = title만 뽑아냄
        title = item.select("a font.list_title")[0].text.strip() # 양쪽 공백제거 되고 , css문법을 다 제거 되서 문자열만 반환
        link = item.select("a font.list_title")[0].parent.get("href").strip()
        link = link.replace("/zboard/","")
        link = link.lstrip("/")
        link = 'https://www.ppomppu.co.kr/zboard/' + link 
        replay_count = item.select("td span.list_comment2 span")[0].text.strip()
        up_count = item.select("td.eng.list_vspace")[-2].text.strip()
        print(up_count)
        if up_count >=3:
            # 터미널 프린트
            print(img_url, title, replay_count, link ,up_count)
    except Exception as e:
        continue


