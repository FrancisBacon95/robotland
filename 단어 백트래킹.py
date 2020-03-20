#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv('네이버맵_리뷰.csv',encoding='ms949')
data


# In[35]:


height_data=pd.DataFrame(columns=['review','star','date'])
limit_data=pd.DataFrame(columns=['review','star','date'])
height_limit_data=pd.DataFrame(columns=['review','star','date'])


# In[36]:


for i in range(0,len(data)):
    if '키' in data.iloc[i][0] and '제한' not in data.iloc[i][0] :
        height_data.loc[len(height_data)]=data.loc[i].tolist()
    elif '제한' in data.iloc[i][0] and '키' not in data.iloc[i][0] :
        limit_data.loc[len(limit_data)]=data.loc[i].tolist()
    elif '제한' in data.iloc[i][0] and '키' in data.iloc[i][0] :
        height_limit_data.loc[len(height_limit_data)]=data.loc[i].tolist()


# # 키 추출

# In[37]:


height_data


# # 제한 추출

# In[38]:


limit_data


# # 키제한 추출

# In[39]:


height_limit_data


# # 놀이기구, 체험 추출

# In[4]:


play_data=pd.DataFrame(columns=['review','star','date'])
exp_data=pd.DataFrame(columns=['review','star','date'])
play_exp_data=pd.DataFrame(columns=['review','star','date'])
for i in range(0,len(data)):
    if '놀이기구' in data.iloc[i][0] and '체험' not in data.iloc[i][0] :
        play_data.loc[len(play_data)]=data.loc[i].tolist()
    elif '체험' in data.iloc[i][0] and '놀이기구' not in data.iloc[i][0] :
        exp_data.loc[len(exp_data)]=data.loc[i].tolist()
    elif '체험' in data.iloc[i][0] and '놀이기구' in data.iloc[i][0] :
        play_exp_data.loc[len(play_exp_data)]=data.loc[i].tolist()


# In[5]:


play_data


# In[6]:


exp_data


# In[7]:


play_exp_data


# In[16]:


summary_data=pd.DataFrame(columns=['키워드','개수','평점'])
summary_data.loc[0]=['놀이기구',len(play_data),play_data['star'].mean()]
summary_data.loc[1]=['체험',len(exp_data),exp_data['star'].mean()]
summary_data.loc[2]=['중복',len(play_exp_data),play_exp_data['star'].mean()]
summary_data


# # 평점 3점 미만 데이터 추출

# In[30]:


down3_data=pd.DataFrame(columns=['review','star','date'])
for i in range(0,len(data)):
    if data.iloc[i][1] < 3 :
        down3_data.loc[len(down3_data)]=data.loc[i].tolist()


# In[31]:


down3_data


# In[32]:


down3_height_data=pd.DataFrame(columns=['review','star','date'])
down3_limit_data=pd.DataFrame(columns=['review','star','date'])
down3_height_limit_data=pd.DataFrame(columns=['review','star','date'])

for i in range(0,len(down3_data)):
    if '키' in down3_data.iloc[i][0] and '제한' not in down3_data.iloc[i][0] :
        down3_height_data.loc[len(down3_height_data)]=down3_data.loc[i].tolist()
    elif '제한' in down3_data.iloc[i][0] and '키' not in down3_data.iloc[i][0] :
        down3_limit_data.loc[len(down3_limit_data)]=down3_data.loc[i].tolist()
    elif '제한' in down3_data.iloc[i][0] and '키' in down3_data.iloc[i][0] :
        down3_height_limit_data.loc[len(down3_height_limit_data)]=down3_data.loc[i].tolist()


# In[33]:


down3_height_data


# In[34]:


down3_limit_data


# In[35]:


down3_height_limit_data

