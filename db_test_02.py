from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient  

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbwhacha                  

path = "C:/Users/yeony/Desktop/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://play.watcha.net/explore?genre=487524")

driver.implicitly_wait(1)

# # TV프로그램 페이지 들어가기
# # time.sleep(2)

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

base = #root > div.css-1v324cc-Self.e19xg79h0 > main > div > section > ul > li:nth-child(261) > div.css-1c7lx0y-Self-Row.e17mfvby0 > ul > li:nth-child(3) > div >

titlea = soup.select_one('')

#root > div.css-1v324cc-Self.e19xg79h0 > main > div > section > ul > li:nth-child(261) > div.css-1c7lx0y-Self-Row.e17mfvby0 > ul > li:nth-child(3) > div > div.css-up0rlb-StillcutContainer.emn3bqe15 > div.css-4v2gg6-DefaultContentWrapper.emn3bqe7 > div.emn3bqe14.css-8cx14e-Self-StillCut.e1q5rx9q0 > span


#root > div.css-1v324cc-Self.e19xg79h0 > main > div > section > ul > li:nth-child(261) > div.css-1c7lx0y-Self-Row.e17mfvby0 > ul > li:nth-child(3) > div > div.css-18mn35g-ContentTitleWrapper.emn3bqe6 > div > div

# DB에 타이틀, 스틸컷 url 저장하기
# for i in range(0,100):
#     for j in range(0, 4):

#         titleA = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text

#         imgA = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > img')

#         urlA = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a')

#         # print(titleA, imgA['src'], urlA['href'])  

#         groupA = {'title':titleA, 'img':imgA['src'], 'url':urlA['href']}
#         db.tvprogram.insert_one(groupA)

# print('1-99번째 DB저장 완료')


# for i in range(100,200):
#     for j in range(0, 4):

#         titleB = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text

#         imgB = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > img')

#         urlB = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a')

#         # print(titleB, imgA['src'], urlB['href'])       
#         groupB = {'title':titleB, 'img':imgB['src'], 'url':urlB['href']}
#         db.tvprogram.insert_one(groupB)

# print('100-199번째 DB저장 완료')


# for i in range(200,300):
#     for j in range(0, 4):

#         titleC = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text

#         imgC = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > img')

#         urlC = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a')

#         # print(titleC, imgC['src'], urlC['href'])       
#         groupC = {'title':titleC, 'img':imgC['src'], 'url':urlC['href']}
#         db.tvprogram.insert_one(groupC)

# print('200-299번째 DB저장 완료')


# for i in range(300,375):
#     for j in range(0, 4):

#         titleD = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text

#         imgD = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > img')

#         urlD = soup.select_one('#title-card-'+ str(i) +'-'+ str(j) +' > div.ptrack-content > a')

#         # print(titleD, imgD['src'], urlD['href'])

#         groupD = {'title':titleD, 'img':imgD['src'], 'url':urlD['href']}
#         db.tvprogram.insert_one(groupD)

# print('300-374번째 DB저장 완료')


# print(">>>>>>>>>>>>> D B 저 장 완 료 ! ! ! !")


# 크롬 종료
# driver.quit()


