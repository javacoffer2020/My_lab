#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import apriori

Transactions = pd.read_csv('Transactions.csv')
Transactions.head()


# In[3]:


baskets = Transactions['Model'].groupby(Transactions['OrderNumber']).apply(list)
baskets.head()


# In[4]:


dataSet = baskets.tolist()


# In[7]:


rules = apriori.arules(dataSet, min_support=0.02)
rules.head()


# In[10]:


contf = rules[(rules.confidence > 0.5) & (rules.lift > 1)]
contf.sort_values(by='support', ascending=True).head()


# In[ ]:




