#!/usr/bin/env python
# coding: utf-8

# # Objects and Data Structures Assessment Test

# ## Test your knowledge. 
# 
# ** Answer the following questions **

# Write a brief description of all the following Object Types and Data Structures we've learned about: 

# Numbers: This data type is divided into 2 categories:- integer and float where integer deals the perfect no. and float deals with decimal number.
# 
# Strings: This data type deals with the alphabetical parts surrounded by single or double inverted commas.
# 
# Lists: This data type deals with the ordered hetrogeneous elements surrounded by []. This data type is mutable data type.
# 
# Tuples: This data type deals with the ordered hetrogeneous elements surrounded by (). This data type is immutable data type.
# 
# Dictionaries: This data type contains keys and values seperated by ':' and surrounded by {} . This data type is mutable data type and contains hetrogeneous elements 
# 

# ## Numbers
# 
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# 
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

# In[2]:


(((12/2-1)*2)**2)+0.25


# Answer these 3 questions without typing code. Then type code to check your answer.
# 
#     What is the value of the expression 4 * (6 + 5) --> 44
#     
#     What is the value of the expression 4 * 6 + 5 --> 29
#     
#     What is the value of the expression 4 + 6 * 5 --> 34

# In[8]:


print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)


# What is the *type* of the result of the expression 3 + 1.5 + 4?<br><br>float

# What would you use to find a number’s square root, as well as its square? 

# In[9]:


# Square root: **.5  


# In[56]:


# Square: **2


# ## Strings

# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

# In[10]:


s = 'hello'
# Print out 'e' using indexing
s[1]


# Reverse the string 'hello' using slicing:

# In[11]:


s ='hello'
# Reverse the string using slicing

s[::-1]


# Given the string hello, give two methods of producing the letter 'o' using indexing.

# In[12]:


s ='hello'
# Print out the 'o'

# Method 1:
s[4]


# In[13]:


# Method 2:

s[-1]


# ## Lists

# Build this list [0,0,0] two separate ways.

# In[15]:


# Method 1:
list=[0,0,0]
list


# In[23]:


# Method 2:
list1=[]
list1.append(0)
list1.append(0)
list1.append(0)
list1


# Reassign 'hello' in this nested list to say 'goodbye' instead:

# In[25]:


list3 = [1,2,[3,4,'hello']]

list3[2][2]='goodbye'
list3


# Sort the list below:

# In[26]:


list4 = [5,3,4,6,1]

list4.sort()
list4


# ## Dictionaries

# Using keys and indexing, grab the 'hello' from the following dictionaries:

# In[32]:


d = {'simple_key':'hello'}
# Grab 'hello'
d['simple_key']


# In[33]:


d = {'k1':{'k2':'hello'}}
# Grab 'hello'
d['k1']['k2']


# In[1]:


# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello

d['k1'][0]['nest_key'][1]


# In[55]:


# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d['k1'][2]['k2'][1]['tough'][2]


# Can you sort a dictionary? Why or why not?<br><br>
# No, we can not sort the dictionary because of two reasons:-
# 1) Dictionary contains keys and values which is seperated by ':'. 
# 2) contains hetrogeneous elements which is imposible to sort.

# ## Tuples

# What is the major difference between tuples and lists?<br><br>
# Tuples are of immutable data type whereas
# 
# Lists are of mutable data type

# How do you create a tuple?
# a=tuple(2,5,8,9)
# print(a)

# ## Sets 

# What is unique about a set?<br><br>

# Use a set to find the unique values of the list below:

# In[ ]:


list5 = [1,2,2,33,4,4,11,22,3,3,2]




# ## Booleans

# For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.
# 
# <table class="table table-bordered">
# <tr>
# <th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
# </tr>
# <tr>
# <td>==</td>
# <td>If the values of two operands are equal, then the condition becomes true.</td>
# <td> (a == b) is not true.</td>
# </tr>
# <tr>
# <td>!=</td>
# <td>If values of two operands are not equal, then condition becomes true.</td>
# <td> (a != b) is true.</td>
# </tr>
# <tr>
# <td>&gt;</td>
# <td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
# <td> (a &gt; b) is not true.</td>
# </tr>
# <tr>
# <td>&lt;</td>
# <td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
# <td> (a &lt; b) is true.</td>
# </tr>
# <tr>
# <td>&gt;=</td>
# <td>If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &gt;= b) is not true. </td>
# </tr>
# <tr>
# <td>&lt;=</td>
# <td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &lt;= b) is true. </td>
# </tr>
# </table>

# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# In[ ]:


# Answer before running cell
2 > 3


# In[ ]:


# Answer before running cell
3 <= 2


# In[ ]:


# Answer before running cell
3 == 2.0


# In[ ]:


# Answer before running cell
3.0 == 3


# In[ ]:


# Answer before running cell
4**0.5 != 2


# Final Question: What is the boolean output of the cell block below?

# In[ ]:


# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']


# ## Great Job on your first assessment! 
