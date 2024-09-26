#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Submissions are evaluated on Root-Mean-Squared-Error (RMSE) between the logarithm of the predicted value and the logarithm of the observed sales price. (Taking logs means that errors in predicting expensive houses and cheap houses will affect the result equally.)


# In[3]:


import pandas as pd 


# In[4]:


import os


# In[9]:


print(os.getcwd())


# In[11]:


os.chdir('/Users/sijan/Documents/GitHub/ML-Voyagers/Data')


# In[12]:


dataset = pd.read_csv('train.csv')


# In[17]:


print(dataset.head())


# In[18]:


print(dataset.columns)


# In[19]:


dataset


# In[21]:


print(dataset['Neighborhood'].unique())


# In[23]:


print(dataset['BldgType'].unique())


# In[24]:


print(dataset['SaleCondition'].unique())


# In[ ]:


##Check for missing values?? 


# In[25]:


## Histogram for interesting looking variables???


# In[27]:


## Past sale prices
print(dataset['SalePrice'].describe())


# In[28]:


# What kind of different areas are the houses located in? 
# What kind of amenities are in nearby areas? 


# In[ ]:




