import requests
import os, time, sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# launch chrome browser
driver = webdriver.Chrome()
# google image search
driver.get('https://www.google.co.jp/imghp?hl=ja&tab=wi&ogbl')
# execute search
keyword = sys.argv[1]
driver.find_element_by_name('q').send_keys(keyword, Keys.ENTER)

current_url = driver.current_url
html = requests.get(current_url)
bs = BeautifulSoup(html.text, 'lxml')
images = bs.find_all('img', limit=10)

os.makedirs(keyword)
WAIT_TIME = 1

for i, img in enumerate(images, 1):
    src = img.get('src')
    response = requests.get(src)
    with open(keyword + '/' + '{}.jpg'.format(i), 'wb') as f:
        f.write(response.content)
    time.sleep(WAIT_TIME)

driver.quit()