# To Do
- I downloaded the image data using the Flickr API in ['py_flickr'](https://github.com/hiraku00/py_flickr),  
but this time I will download the image data using Google Image Search.
- Launch Chrome using Selenium WebDriver and automate the search operation on Google image search screen.

# Summary
- 1. Import library
- 2. Run Google Image Search
- 3. Scraping search results
- 4. Download image data

# Operating Environment
- macOS Catalina 10.15 beta
- google chrome 75.0.3770.142
- Python 3.6.8
- beautifulsoup4 4.8.0
- selenium 3.141.0
- python-chromedriver-binary 2.38.0
- lxml 4.3.4
- requests 2.21.0

# 1. Import library
- Import the following library

```python:library
import requests
import os, time, sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```

# 2. Run Google Image Search
- Launch Chrome and open Google Image Search screeen.
- After that, enter a keyword in the search form, and then press the enter key.  
(the ketword is specified at the time of program execution)
- Specify 'q' for 'find_element_by_name'.(check the search form name attribute as fellow)
<img width="1191" alt="1.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/67194/74da864d-120d-5c9d-a175-9dc77d186d18.png">

```python:2.Run Google Image Search
# launch chrome browser
driver = webdriver.Chrome()
# google image search
driver.get('https://www.google.co.jp/imghp?hl=ja&tab=wi&ogbl')
# execute search
keyword = sys.argv[1]
driver.find_element_by_name('q').send_keys(keyword, Keys.ENTER)
```

# 3. Scraping search results
- Specify the URL of the search result screen and get the information of html.
- Analyze using BeautifulSoup. And specify lxml for HTML parser.
- Get 10 'img' tags

```python:3.Scraping search results
current_url = driver.current_url
html = requests.get(current_url)
bs = BeautifulSoup(html.text, 'lxml')
images = bs.find_all('img', limit=10)
```
- The 'img' tag is stored in images as follows.

```python
[<img alt="「XXX」の画像検索結果" height="XXX" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:XXXYYYZZZ1" width="XXX"/>,
 <img alt="「XXX」の画像検索結果" height="XXX" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:XXXYYYZZZ2" width="XXX"/>,
 <img alt="「XXX」の画像検索結果" height="XXX" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:XXXYYYZZZ3" width="XXX"/>,
 <img alt="「XXX」の画像検索結果" height="XXX" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:XXXYYYZZZ4" width="XXX"/>,
 <img alt="「XXX」の画像検索結果" height="XXX" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:XXXYYYZZZ5" width="XXX"/>,
 <img alt="「XXX」の画像検索結果" height="XXX" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:XXXYYYZZZ6" width="XXX"/>,
 <img alt="「XXX」の画像検索結果" height="XXX" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:XXXYYYZZZ7" width="XXX"/>,
 <img alt="「XXX」の画像検索結果" height="XXX" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:XXXYYYZZZ8" width="XXX"/>,
 <img alt="「XXX」の画像検索結果" height="XXX" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:XXXYYYZZZ9" width="XXX"/>,
 <img alt="「XXX」の画像検索結果" height="XXX" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:XXXYYYZZZ10" width="XXX"/>]
```

# 4. Download image data
- First, create a directory to save. The name of the directory is search keyword.
- Get 'src' attribute in 'img' tag to get image data.  
(Refer to the contents of images in [3.])
- Get image data with 'requests.get'.
- Declare writting with sequential number (starting index is '1') in the search keyword directory with 'with open'. 

- Write responce (image data) with 'f.write'.
- After downloading 1 file, wait 1 second to space between requests in order to reduce server load.  
(stop for 1 second with 'time.sleep')
- Close the browse when finished.

```python:4.Download image data
os.makedirs(keyword)
WAIT_TIME = 1

for i, img in enumerate(images, 1):
    src = img.get('src')
    response = requests.get(src)
    with open(keyword + '/' + '{}.jpg'.format(i), 'wb') as f:
        f.write(response.content)
    time.sleep(WAIT_TIME)

driver.quit()
```

# Execute code
- Specify search keyword at execution.(XXXX part)

```terminal:Execute code
$ python py_scrayping.py XXXX
```

# in Japanese
- [Qiita](https://qiita.com/hiraku00/items/1f71fa2bab8e0f58cdcf)
