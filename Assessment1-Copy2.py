#!/usr/bin/env python
# coding: utf-8

# ASSESSMENT- Getting and Knowing your Data

# 
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# In[2]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'


# ### Step 3. Assign it to a variable called users and use the 'user_id' as index

# In[3]:


users = pd.read_csv(url, delimiter = '|')
users = users.set_index('user_id')
users


# ### Step 4. See the first 25 entries

# In[4]:


users.head(25)


# ### Step 5. See the last 10 entries

# In[5]:


users.tail(10)


# ### Step 6. What is the number of observations in the dataset?

# In[6]:


users.shape[0]


# ### Step 7. What is the number of columns in the dataset?

# In[7]:


users.shape[1]


# ### Step 8. Print the name of all the columns.

# In[8]:


users.columns


# ### Step 9. How is the dataset indexed?

# In[9]:


users.index


# ### Step 10. What is the data type of each column?

# In[10]:


users.info()


# ### Step 11. Print only the occupation column

# In[11]:


users['occupation']  


# ### Step 12. How many different occupations are in this dataset?

# In[12]:


count = users.occupation.value_counts()
count


# In[13]:


len(count)


# ### Step 13. What is the most frequent occupation?

# In[14]:


users.occupation.value_counts().head(1)


# ### Step 14. Summarize the DataFrame.

# In[15]:


users.describe()


# ### Step 15. Summarize all the columns

# In[16]:


users.describe(include = 'all')


# ### Step 16. Summarize only the occupation column

# In[17]:


users.occupation.describe()


# ### Step 17. What is the mean age of users?

# In[18]:


users.age.mean()


# ### Step 18. What is the age with least occurrence?

# In[19]:


users.age.value_counts().tail(1)


# ### Step 19. Write a lambda function to convert a string column to a numerical column 

# In[20]:


fun = lambda to_num : pd.to_numeric(to_num) if type(to_num) is int else to_num


# In[21]:


users = users.apply(fun)


# In[25]:


users.head(10)


# In[ ]:





# In[ ]:





# In[ ]:




