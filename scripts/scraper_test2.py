#웹 스크래핑 코드
#텔레그램 push


#https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu
import requests
from bs4 import BeautifulSoup
import telegram
import teltram_info



TLGM_BOT_API = teltram_info.TLGM_BOT_API
tlgm_bot = telegram.Bot(TLGM_BOT_API) # api를 가진 텔레그램 봇 객체 생성



# 요청보내기
url = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu'
res = requests.get(url)
# print(res)
# print(res.text)

soup = BeautifulSoup(res.text,"html.parser")
#print(soup)

items = soup.select("tr.list1,tr.list0")

# img_url, title, link, replay_count, up_count을 스크래핑.
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
        up_count = up_count.split("-")[0]
        up_count = int(up_count)

        print(up_count)
        if up_count >=3: # 추천인 3개이상일 때
            # 터미널 프린트
            print(img_url, title, replay_count, link ,up_count)
            #텔레그램 봇에 출력
            # tlgm_bot.sendMessage(chat_id, message)
            chat_id = teltram_info.chat_id
            message = title
            
            tlgm_bot.sendMessage(chat_id, message)
    except Exception as e:
        continue


