from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient  


client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbnetflixTV                  

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

# print('스크롤 완료 !')
# =========================================================================


soup = BeautifulSoup(driver.page_source, 'html.parser')

# DB에 타이틀, 스틸컷 url 저장하기
for i in range(0,100):
    for j in range(0, 4):

        titleA = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text

        imgA = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > img')

        urlA = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a')

        # print(titleA, imgA['src'], urlA['href'])  

        groupA = {'title':titleA, 'img':imgA['src'], 'url':urlA['href']}
        db.tvprogram.insert_one(groupA)

print('1-99번째 DB저장 완료')


for i in range(100,200):
    for j in range(0, 4):

        titleB = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text

        imgB = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > img')

        urlB = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a')

        # print(titleB, imgA['src'], urlB['href'])       
        groupB = {'title':titleB, 'img':imgB['src'], 'url':urlB['href']}
        db.tvprogram.insert_one(groupB)

print('100-199번째 DB저장 완료')


for i in range(200,300):
    for j in range(0, 4):

        titleC = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text

        imgC = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > img')

        urlC = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a')

        # print(titleC, imgC['src'], urlC['href'])       
        groupC = {'title':titleC, 'img':imgC['src'], 'url':urlC['href']}
        db.tvprogram.insert_one(groupC)

print('200-299번째 DB저장 완료')


for i in range(300,375):
    for j in range(0, 4):

        titleD = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text

        imgD = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > img')

        urlD = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a')

        # print(titleD, imgD['src'], urlD['href'])

        groupD = {'title':titleD, 'img':imgD['src'], 'url':urlD['href']}
        db.tvprogram.insert_one(groupD)

print('300-374번째 DB저장 완료')


print(">>>>>>>>>>>>> D B 저 장 완 료 ! ! ! !")


# 크롬 종료
driver.quit()



# 해야할것 1.db 저장 2.db/html 연결  3.서버-클라이언트 연결 (넷플릭스(에서 tv프로그램)만 진행)
# 1-1. 목록 주소를 sort로 나눠서 반복문 돌리기 >> 문제발생 url 끝자락 변화로 링크가 안됨
# 1-2. DB 저장을 우선으로 하기 > pymongo 부터 진행
# 1-3. 반복문 숫자를 나눠서 돌려보기 총 row4*coloum375=1500개 (무한스크롤이 있어야 중간에러 안남)
# 
