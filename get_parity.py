#!/usr/bin/env python
# coding: utf-8

# In[7]:


s1='четное'
s2='нечетное'
s3='Введите целое число'
def get_parity(x):
    if type(x)==int:
        if x%2==0:
            return s1
        else:
            return s2
    else:
        return s3

