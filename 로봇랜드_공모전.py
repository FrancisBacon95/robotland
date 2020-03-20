#!/usr/bin/env python
# coding: utf-8

# In[12]:


from selenium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions는 Selenium 2.26.0 이후 부터 사용 가능합니다.
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from time import sleep


# In[14]:


driver=webdriver.Chrome(executable_path="chromedriver.exe")
url="https://m.place.naver.com/place/1155084898/review/booking"
driver.get(url)
driver.close()


# In[85]:


while True :
    if driver.find_element_by_xpath('//*[@id="app-root"]/div[2]/div[4]/div[2]/div[4]/div[2]/a').text == "더보기" :
        driver.find_element_by_xpath('//*[@id="app-root"]/div[2]/div[4]/div[2]/div[4]/div[2]/a').click()
        sleep(0.5)
    else :
        break


# In[100]:


naver_map_review_pd=pd.DataFrame([[0,0,0]],columns=['title','date','link'])
naver_map_review_list=driver.find_elements_by_xpath('//*[@id="app-root"]/div[2]/div[4]/div[2]/div[4]/div/ul/li')
for item in naver_map_review_list :
    review=item.find_element_by_xpath('.//div/div[2]/a/span').text
    star=item.find_element_by_xpath('./div/div[1]/span[2]').text
    date=item.find_element_by_xpath('./div/div[3]/span[2]').text.split(' ')[0]
    naver_map_review_pd.loc[len(naver_map_review_pd)]=[review,star,date]
naver_map_review_pd


# In[114]:


naver_map_review_pd.to_csv('네이버맵_리뷰.csv',encoding='utf-8')


# In[54]:


data=pd.read_csv('네이버맵_리뷰.csv',encoding='ms949')
data


# In[100]:


from konlpy.tag import Twitter
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from collections import Counter
komoran=Komoran()
stopword=pd.read_csv('한글_불용어(중복제거).csv',encoding='ms949')['불용어'].tolist()


# In[108]:


nouns_list=[]
for item in data['title'] :
    nouns=komoran.nouns(item)
    for noun in nouns :
        nouns_list.append(noun)


# In[115]:


count=Counter(nouns_list)
counting_data=pd.DataFrame(count.most_common(200),columns=['단어','카운트'])


# In[118]:


no_stop_counting_data=pd.DataFrame(columns=['단어','카운트'])


# In[130]:


no_stop_counting_list=[]
for i in range(0,len(count.most_common(200))-1) :
    if count.most_common(200)[i][0] not in stopword and count.most_common(200)[i][0] not in ['거','탈수','수','번','살','곳','넘','듯','시','건','그런지','꺼','요','점','이랑','완전','간','한','분','도','게','!!','중','때문','편','전반','관','담','기','학','아이와','데','날','부분','관이','말','습','데리','감바','가지','못','문','면','건지','우','바','지','되','컷']:
         no_stop_counting_list.append(count.most_common(200)[i])       


# In[136]:


no_stop_counting_pd=pd.DataFrame(no_stop_counting_list,columns=['단어','카운트'])
no_stop_counting_pd[:99].to_csv('네이버맵_리뷰_탑100.csv',index=False,encoding='ms949')


# In[116]:


counting_data.to_csv('탑200단어.csv',encoding='ms949',index=False)


# In[138]:


get_ipython().system('pip install wordcloud')


# In[156]:


from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# In[157]:


mask = np.array(Image.open('./로봇로고.jpg'))


# In[165]:


wc = WordCloud(font_path='C:/windows/Fonts/malgun.ttf', background_color="white",mask=mask).generate_from_frequencies(dict(no_stop_counting_list))


# In[166]:


wc.to_file('test.png')


# In[ ]:




