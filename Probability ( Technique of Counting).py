#!/usr/bin/env python
# coding: utf-8

# In[15]:


#  No of possible probability of arranging number of set ( sample size= n, number of selection= r) with order respect, without repetitation
def factorial(n):
    if n==1: return 1
    else: return n * factorial(n-1)
def permutation_no_rep (n,r):
    return(factorial(n)/factorial(n-r))
# No of possible probability with order respect,with repetitation
def permutation_rep (n,r):
    return(n**r)
# No of possible probability without order, with repetitation
def combination_rep (n,r):
    return((factorial(n+r-1))/(factorial(r)*factorial(n-1)))
# No of possible probability without order, without repetitation
def combination_no_rep (n,r):
      return(((factorial(n)/(factorial(r))*(factorial (n-r)))))
# car plat with 6 digit (3 letter+ 3 number) no duplicated letter or number.
# the number of plates can be formed are= p(letter).p(number)
p_letter = permutation_no_rep (26,3)
p_number = permutation_no_rep(10,3)
print(p_letter* p_number)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




