from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbnetflix                   # 'dbsparta'라는 이름의 db를 만듭니다.

usr = 'synyout@gmail.com'
pwd = 'qlalf2424.'

path = "C:/Users/yeony/Desktop/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://www.netflix.com/kr/login")

assert "Netflix" in driver.title  
# ??????????????????????????? 가정설정문?? 왜??

elem = driver.find_element_by_name('userLoginId')
elem.send_keys(usr)
elem = driver.find_element_by_name('password')
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

driver.implicitly_wait(1)

# TV프로그램 페이지 들어가기
driver.get('https://www.netflix.com/browse/genre/83')
driver.get('https://www.netflix.com/browse/genre/83?so=az')
# sort=['ad','eh','il','mp','qu','vz']

# time.sleep(2)

# 무한스크롤 =====================================================================
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
# =========================================================================


soup = BeautifulSoup(driver.page_source, 'html.parser')


# 반복문

# for i in range(0,375, 1):
#     for j in range(0, 4):

#         titles = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text


# imgurlsA = soup.select_one('#title-card-0-1 > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > img')
# src = imgurlsA
# print(imgurlsA, src)



for i in range(0,100):
    for j in range(0, 4):

        titlesA = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text
        print(titlesA)

        # imgurlsA = soup.select_one('#title-card-0-0 > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > img[src]').text
        # linksA = soup.select_one('')  , 'imgurl':imgurlsA, 'link':linksA
        groupA = {'title':titlesA}
        db.tvprogram.insert_one(groupA)


for i in range(100,200):
    for j in range(0, 4):

        titlesB = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text
        # print(titlesB)

        groupB = {'title':titlesB}
        db.tvprogram.insert_one(groupB)


for i in range(200,300):
    for j in range(0, 4):

        titlesC = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text
        # print(titlesC)

        groupC = {'title':titlesB}
        db.tvprogram.insert_one(groupC)

for i in range(300,375):
    for j in range(0, 4):

        titlesD = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text
        print(titlesD)

        groupD = {'title':titlesD}
        db.tvprogram.insert_one(groupD)

        print(">>>>>>>>>>>>> D B 저 장 완 료 ! ! ! !")


# 크롬 종료
driver.quit()



# 해야할것 1.db 저장 2.db/html 연결  3.서버-클라이언트 연결 (넷플릭스(에서 tv프로그램)만 진행)
# 1-1. 목록 주소를 sort로 나눠서 반복문 돌리기 >> 문제발생 url 끝자락 변화로 링크가 안됨
# 1-2. DB 저장을 우선으로 하기 > pymongo 부터 진행
# 1-3. 반복문 숫자를 나눠서 돌려보기 총 row4*coloum375=1500개 (무한스크롤이 있어야 중간에러 안남)
# 
