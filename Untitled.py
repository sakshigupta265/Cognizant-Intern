#!/usr/bin/env python
# coding: utf-8

# In[7]:


n = int(input())
ans = []
for i in range(0,2**n):
    a = [i//2**j%2 for j in reversed(range(0,n))]
    ans.append(a)
for i in range(0,len(ans)):
    print(*ans[i],sep='')

