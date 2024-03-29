#웹 스크래핑 코드
#텔레그램 push
#DB로 저장하기

#https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu
import requests
from bs4 import BeautifulSoup
import telegram
# import teltram_info django.extensions 설치전
# from . import teltram_info django.extensions 설치후
import env_info
from hordeal.models import Deal
from datetime import datetime, timedelta

# db 테이블 데이터 유지기간 설정 변수
during_date = 3
#db 테이블 저장을 휘한 추천 개수 지정(3개이상) ,유지보수하기 쉬운 방법
up_count_limit=3

TLGM_BOT_API = env_info.TLGM_BOT_API
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
def run():
     #DB에 저장되는 데이터가 3시간만 유지

    # row, _= Deal.objects.filter(cdate__lte = datetime.now() - timedelta(days=3)).delete()
    row, _= Deal.objects.filter(cdate__lte = datetime.now() - timedelta(minutes = during_date)).delete()
    print(row,"deals deleted")
    
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

        
            # print(up_count)
            if up_count >=up_count_limit: # 추천인 3개이상일 때
                # 터미널 프린트
                print(img_url, title, replay_count, link ,up_count)
                #텔레그램 봇에 출력
                # tlgm_bot.sendMessage(chat_id, message)
                chat_id = env_info.chat_id
                message = title
                
                tlgm_bot.sendMessage(chat_id, message)

                # hot deal 앱의 Deal클래스를 통해 DB 테이블에 데이터 저장
                if(Deal.objects.filter(link__iexact=link).count()==0): #iexat: 대소문자 구분하디 않고 정확히 일치하는 데이터찾기
                    Deal(img_url=img_url, title=title, link=link,
                    # 스크래핑 결과를 DB의 Deal 테이블에 저장
                        replay_count=replay_count, up_count=up_count).save()
            
        except Exception as e:
            continue
