
for i in range(0,375, 1):
    for j in range(0, 4):
        print("#title-card-%d-%d"%(i,j))


# print(,end='')


# titlea = soup.select_one('#title-card-0-0 > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text

# titleb = soup.select_one('#title-card-0-1 > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text

# titlec = soup.select_one('#title-card-0-2 > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text

# titled = soup.select_one('#title-card-0-3 > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text

# titlelasta = soup.select_one('#title-card-374-0 > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text

# titlelastd = soup.select_one('#title-card-374-3 > div.ptrack-content > a > div.boxart-size-16x9.boxart-container > div > p').text


# print(titlea, titleb, titlec, titled, titlelasta, titlelastd)


# 무한스크롤 =====================================================================
# https://www.it-swarm.dev/ko/python/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-selenium-%EC%9B%B9-%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B2%84%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-%EC%9B%B9-%ED%8E%98%EC%9D%B4%EC%A7%80%EB%A5%BC-%EC%8A%A4%ED%81%AC%EB%A1%A4%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9E%85%EB%8B%88%EA%B9%8C/1044180775/

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