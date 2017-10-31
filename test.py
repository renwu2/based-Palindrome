
# coding: utf-8

# In[6]:


import string
digs = string.digits+string.ascii_letters


# In[7]:


def int2base(n,base):
    if base == 10:
        return str(n)
    if n <0:
        sign = -1
    elif n==0:
        return '0'
    else:
        sign = 1
    n*=sign
    res = []
    while n:
        #print(n%base)
        res.append(digs[n%base])
        n = int(n/base)
        #print(n)
    if sign<0: res.append('-')
    res = res[::-1]
    return ''.join(res)


# In[11]:


def is_pali(s):
    return s==s[::-1]


# In[32]:


def find_smallest_base(n):
    if n==0:return 0
    if n==1:return 2
    for base in range(2,len(digs)):
        s = int2base(n,base)
        if s == s[::-1]:
            return int(base)


# In[33]:


list(map(find_smallest_base,list(range(1,1000))))


# In[14]:





# In[ ]:




