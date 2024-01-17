#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[15]:


df=pd.read_csv("C:/Users/USER/Downloads/note 13.csv")


# In[47]:


d={x*2: x for x in range(8)}


# In[50]:


print(d)
print(d[0])
print(d[2])
print(d[4])
print(d[6])
#0,2,4,6 are keys. 0,1,2,3 are values. values comes as output.


# In[52]:


d.items()
print(d.items())
#print(d.items()) gives you a view of the (key-value) pairs in the dictionary.


# In[17]:


print(df)


# In[56]:


s={8,10,11,12,13,14}
u={12,13,14,15,16,17}
s.difference(u)
#is used to find the elements that exist in one set (s), but not in another set (u)


# In[57]:


u.difference(s)


# In[58]:


s.difference_update(u)


# In[61]:


print(s,u)


# In[62]:


m=s.copy()


# In[29]:


print(m)


# In[30]:


print(u)


# In[40]:


s.add(9)


# In[39]:


print(s)


# In[43]:


intersection_set=s.intersection(u)


# In[47]:


s.intersection(u)


# In[49]:


s={8,10,11,12,13}
u={0:12,1:13,2:14,3:15,4:16}
s.difference(u)


# In[50]:


s.intersection_update(u)


# In[52]:


print(s,u)


# In[55]:


s.isdisjoint(u)
# returns Boolean o/p if the set has no common elements 


# In[57]:


s.issubset(u)
# returns Boolean o/p if the set has common elements.if the elements of s is present in u, the u is considered as subset of s  


# In[63]:


u.issuperset(s)


# In[65]:


s.pop()


# In[66]:


s.symmetric_difference(u)


# In[68]:


s.union(u)


# In[69]:


print(s,u)


# In[94]:


u={0:12,1:13,2:14,3:15,4:16}


# In[95]:


u.get(2)


#  

# In[8]:


x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
    
#spaces or tabs to after 'if' 'elif' and 'else' to state whether following codes are inside the condition  


# In[9]:


if x<5:
    pass
#Used in empty code blocks in functions or classes that you plan to implement later. 
#To indicate that a particular part of the code is not yet implemented.


# In[67]:


#Looping through Lists and Tuples
a=[0,1,2,3,4,5]


# In[70]:


for x in a: 
    print(x)
    print (x*2)
#print(x): It prints the current number.
#print(x * 2): It prints the current number multiplied by 2 in below.


# In[71]:


#looping through strings 
a="hello"
for x in a:
    print(x)
    # Print the character
    print(x*2)
    #multipies the character and Print


# In[74]:


#break
a="penaten"
for x in a:
    print(x)
    if x=="a":
        break
#here the loop iterates through each character in the string "example".
#It prints each character, and if it encounters the character "a", 
#the loop is terminated using the break statement.


# In[83]:


#continue 
a="penaten"
for x in a:
    if x =="a":
        continue
    print(x)


# In[87]:


#else in for loop
for x in a :
    print(x)
    break
else :
    print("loop finished.")
#here it prints each element of 'x' but after the very first result, the loop did not completes normally; it was terminated by 'break' statement.
#If a break statement is encountered, the else block is skipped.


# In[96]:


#nested loop(a loop inside a loop)
for x in a:
    for y in u:
        print(x, y)
# 'a' ile "p"-k 'u'-ile (16-15)values elaam kodth. 
#and same with "e" and rest all letters. 


# In[99]:


for x in a:
    for y in u:
        print(a,u)
#similar distribution but different calculations and output.


# In[106]:


for x in a:
    pass
#The loop will iterate through each element in the list a, but as there is no specific action defined.
# and Since the 'pass' statement does nothing;  it won't produce any output.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




