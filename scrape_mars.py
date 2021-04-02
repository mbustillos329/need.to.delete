import pandas as pd
from bs4 import BeautifulSoup
import requests
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
from selenium import webdriver

# url
url = 'https://redplanetscience.com/'

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)

# retrieve page
# response = requests.get(url)
html = browser.html

# beautiful soup object
soup = BeautifulSoup(html,'html.parser')

print(soup.prettify())

# iterable list 
results = soup.find_all('div', class_ = 'list_text')
results

# loop through results
for result in results:
    try:
#       identify and return title and paragraph 
        news_title = result.find('div', class_ = 'content_title').text
        news_p = result.find('div', class_ = 'article_teaser_body').text
        
        if (news_title and news_p):
            print('-----------------')
            print(news_title)
            print(news_p)
    except AttributeError as e:
        print(e)

# JPL Mars Space Images - Featured Image

# url
url2 = 'https://spaceimages-mars.com/'
browser.visit(url2)
html = browser.html
soup = BeautifulSoup(html,'html.parser')

# finding image url 
images = soup.find_all('img', class_ = 'headerimage fade-in')
featured_image_url = images[0].get('src')    

print(images)
print(featured_image_url)

# Mars Facts

url3 = 'https://galaxyfacts-mars.com/'
tables = pd.read_html(url3)
tables

#  list to df
df = tables[0]

df= df.T
df.columns = df.iloc[0]
df = df.reset_index()
df

df = df.iloc[1:] 
# df.columns = df.columns.str.replace('Diameter', 'Index')
df

df

html_table = df.to_html()

html_table

