from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
from bs4 import BeautifulSoup

usr = 'synyout@gmail.com'
pwd = 'qlalf2424.'

path = "C:/Users/yeony/Desktop/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://www.netflix.com/kr/login")


assert "Netflix" in driver.title

elem = driver.find_element_by_name('userLoginId')
elem.send_keys(usr)
elem = driver.find_element_by_name('password')
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

driver.implicitly_wait(5)


# TV프로그램 페이지 들어가지

driver.get('https://www.netflix.com/browse/genre/83')
driver.get('https://www.netflix.com/browse/genre/83?so=az')


# driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)

# driver.implicitly_wait(2)

# for i in range(5):
#     driver.find_element_by_tag_name('body').send_keys(Keys.END)
#     driver.implicitly_wait(3)
#     time.sleep(5)

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# posts = soup.select('div.text_exposed_root')

# for post in posts:
#     print(post.text)
