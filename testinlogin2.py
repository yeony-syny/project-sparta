from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
from bs4 import BeautifulSoup

usr = 'synyout@gmail.com'
pwd = 'qlalf2424.'

path = "C:/Users/yeony/Desktop/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://play.watcha.net/sign_in")


assert "whacha" in driver.title

elem = driver.find_element_by_name('eu52ful1')
elem.send_keys(usr)
elem = driver.find_element_by_name('password')
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

driver.implicitly_wait(5)


# <input type="email" value="" name="email" class="e19dfl4j0 css-scyd47-StyledField-EmailField eu52ful1" placeholder="이메일 (example@gmail.com)" autocomplete="off" autofocus="">

# # TV프로그램 페이지 들어가지

# driver.get('https://play.watcha.net/explore')

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
