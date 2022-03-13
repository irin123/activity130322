#!/usr/bin/env python
# coding: utf-8

# ## 1. Complete the following code to find the area of an equilateral triangle. Output should be as displayed

# In[15]:


import math
side = float(input("Enter the side of the equilateral triangle: "))
area = ((math.sqrt(3))/4)*pow(side,2)


# ## 2. Write a program to count the number of each characters in a string

# In[1]:


s=input('Enter string')
count=0
for i in s:
    count=count+1
print('No. of characters in the string=',count)


# ## 3. Write a program to find the area and perimeter of a rectangle using functions

# In[2]:


def rectarea():
    print('The area=',l*b)
def rectperimeter():
    print('The perimeter=',2*(l+b))
    
    
l=int(input('Enter length'))
b=int(input('Enter breadth'))
rectarea()
rectperimeter()


# ## 4. Write a program to print the fibonacci series till a specified number

# In[3]:


n=int(input('Enter the number whose factorial is to be found'))
f=1
for i in range(1,n+1):
    f=f*i
print('Factorial=',f)


# ## 5. Complete the following code to find the minimum of 3 number using conditional statements. Output should be as displayed

# In[4]:


a,b,c = input("Enter three numbers followed by  : ").split()

print("First number :",a)
print("Second number :",b)
print("Third number :",c)
if a==b==c:
     print("Entered numbers are equal!!!")
elif a<b and a<c:
    print(a," is smallest")
elif b<a and b<c:
    print(b," is smallest")
else:
    print(c," is smallest")


# ## 6. Write a program to print star pyramind. The number of rows should be taken as input from the user

# In[18]:


r=int(input('Enter Number of Rows'))
spaces=r-1
for i in range (r):
    for j in range(spaces):
        print(end=' ')
        spaces=spaces-1
        for j in range(i+1):
            print('* ',end='')
        print('\n')


# ## 7. Complete the following code to convert hour into seconds. Output should be as displayed

# In[14]:


def to_seconds(t):
    t=t*60*60
    
    return t
time_in_hours = int(input('Enter time in Hours'))
print(time_in_hours ," Hour is equal to" ,to_seconds(time_in_hours) ," Seconds")


# ## 8. Write a program to print multiplication table as below

# In[15]:


n=int(input('Enter a number to find a multiplication table:'))
for i in range(1,11):
    print(i,' x ',n,' = ',i*n)


# ## 9. Write a program to take your 5 favorite food as list and print each as 'I like Biriyani'

# In[17]:


L=eval(input('Enter 5 favorite foods'))
print('The list is' , L)
for i in L:
    print('I like' ,i )


# In[ ]:




