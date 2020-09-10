#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[12]:


n = 10
np.linalg.solve(np.random.randn(n**2).reshape(n,n),np.random.randn(n,1))


# In[47]:


n = 2
a = np.linalg.matrix_power(np.random.randn(n,n),2)
a[0,0] = 1
a[-1,-1] = -1
b = np.random.randn(n)
b[0] = -1
c = np.linalg.solve(a,b)
s, v, d = np.linalg.svd(a)
print(c)
print(s)
print(v)
print(d)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[42]:


s,v,d = np.linalg.svd(a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[29]:


b


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




