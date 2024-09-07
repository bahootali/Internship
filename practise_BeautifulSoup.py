#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


# importing required libraries
from bs4 import BeautifulSoup
import requests


# In[ ]:


send get requests to the webpage server to get the source code of the page 


# In[ ]:


# 1) Write a python program to display IMDB’s Top rated 100 Indian movies’ data
# https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year ofrelease) and make data frame.


# In[217]:


page = requests.get("https://www.imdb.com/list/ls056092300/")


# In[218]:


page


# In[219]:


soup = BeautifulSoup(page.content)        # it's downloaded page content

soup


# In[ ]:


# 2) Write a python program to scrape details of all the posts from https://www.patreon.com/coreyms.Scrape the
# heading, date, content and the likes for the video from the link for the youtube video from the post.


# In[220]:


page = requests.get("https://www.patreon.com/coreyms")


# In[221]:


page


# In[ ]:


page content


# In[222]:


soup = BeautifulSoup(page.content)        # it's downloaded page content

soup


# In[234]:


first_heading = soup.find('div', class_="sc-bBHxTw jIEOUn")

first_heading


# In[ ]:


# 3) Write a python program to scrape house details from mentioned URL. It should include house title, location,
# area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar,Rajaji Nagar.


# In[193]:


page = requests.get("https://www.nobroker.in/")


# In[194]:


page


# In[ ]:


page content


# In[225]:


soup = BeautifulSoup(page.content)        # it's downloaded page content

soup


# In[ ]:


# 4) Write a python program to scrape first 10 product details which include product name , price , Image URL from
# https://www.bewakoof.com/bestseller?sort=popular .


# In[119]:


page = requests.get("https://www.bewakoof.com/bestseller?sort=popular")

page


# In[ ]:


page content


# In[120]:


soup = BeautifulSoup(page.content)        # it's downloaded page content

soup


# In[123]:


product_name = soup.find('div', class_="productNaming bkf-ellipsis")

product_name


# In[124]:


product_name.text


# In[130]:


prod_name = []

for i in soup.find_all('div', class_="productNaming bkf-ellipsis"):
    prod_name.append(i.text.strip())
    prod_name=prod_name[0:10]
    
prod_name


# In[133]:


prod_price = soup.find('div', class_="discountedPriceText")

prod_price


# In[134]:


prod_price.text


# In[141]:


price = []

for i in soup.find_all('div',class_="discountedPriceText"):
    price.append(i.text)
    price=price[0:10]
        
price


# In[136]:


image_url = soup.find('img', class_="productImgTag")

image_url


# In[137]:


image_url['src']


# In[146]:


prodt_image = []

for i in soup.find_all('img', class_="productImgTag"):
    prodt_image.append(i['src'])
    prodt_image=prodt_image[0:10]
    
prodt_image


# In[ ]:


# 5) Please visit https://www.cnbc.com/world/?region=world
#a) headings
#b) date
#c) News link


# In[156]:


page = requests.get("https://www.cnbc.com/world/?region=world")

page


# In[ ]:


page content


# In[157]:


soup = BeautifulSoup(page.content)        # it's downloaded page content

soup


# In[158]:


headings = []

for i in soup.find_all('div', class_="RiverHeadline-headline RiverHeadline-hasThumbnail"):
    headings.append(i.text)
    
headings


# In[159]:


news_date = []

for i in soup.find_all('span', class_ ="RiverByline-datePublished"):
    news_date.append(i.text) # if date else " "
    
    
news_date


# In[160]:


newslink = []

for i in soup.find_all('div', class_="RiverHeadline-headline RiverHeadline-hasThumbnail"):
    newslink.append(i.a["href"])
    
newslink


# In[80]:





# In[ ]:




