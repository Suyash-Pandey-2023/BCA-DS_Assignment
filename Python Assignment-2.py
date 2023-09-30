#!/usr/bin/env python
# coding: utf-8

# In[1]:


################ Q-1 ################


# In[2]:


Scores=[35,50,20,30,55,75,90,95,66,80]


# In[3]:


#(i)
print(Scores)


# In[4]:


#(ii)
for i in range(0,len(Scores)):
  if Scores[i]>70:
    Scores[i]="distinction"
print(Scores)


# In[5]:


#(iii)
Scores=[35,50,20,30,55,75,90,95,66,80]
for i in range(0,len(Scores)):
  if Scores[i]>=60 and Scores[i]<70:
    Scores[i]="first class"
print(Scores)


# In[6]:


#(iv)
Scores=[35,50,20,30,55,75,90,95,66,80]
for i in range(0,len(Scores)):
  if Scores[i]>=50 and Scores[i]<60:
    Scores[i]="second class"
print(Scores)


# In[7]:


#(v)
Scores=[35,50,20,30,55,75,90,95,66,80]
for i in range(0,len(Scores)):
  if Scores[i]>=35 and Scores[i]<50:
    Scores[i]="just pass"
print(Scores)


# In[8]:


#(vi)
Scores=[35,50,20,30,55,75,90,95,66,80]
for i in range(0,len(Scores)):
  if Scores[i]<50:
    Scores[i]="fail"
print(Scores)


# In[9]:


################ Q-2 ################


# In[10]:


Book_price= {'Python':600, 'Java': 400, 'Web_Tech': 550, 'OS': 450, 'IT': 700}
for i,j in Book_price.items():
  if j>500:
    print(i)


# In[11]:


################ Q-4 ################


# In[12]:


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
for i in list1:
  for j in list2:
    print(i+j)


# In[13]:


################ Q-5 ################


# In[14]:


a=[100, 200, 300, 400, 500]
a[::-1]


# In[15]:


################ Q-6 ################


# In[16]:


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
list1


# In[17]:


################ Q-7 ################


# In[18]:


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend(["i","j","k"])
list1


# In[19]:


################ Q-8 ################


# In[20]:


list1 = [5, 10, 15, 20, 25, 50, 20]
list1[3]=200
print(list1)


# In[21]:


################ Q-9 ################


# In[22]:


Player_game={'Sachin':'Cricket', 'Rahul': 'Cricket', 'Messi': 'Football', 'Federer': 'Tennis', 'Anand': 'Chess'}
for i,j in Player_game.items():
  if j=="Cricket":
    print(i)


# In[23]:


################ Q-10 ################


# In[24]:


List1= [1,2,4,5,10,20,4,5]
b=0
for i in range(0,len(List1)):
  b+=List1[i]
print(b)


# In[ ]:




