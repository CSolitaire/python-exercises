#!/usr/bin/env python
# coding: utf-8

# In[1]:



word = 'corey solitaire'
new_word = []
vowel = set('aeiou')
def letter_search (word):
    for letter in word:
        if letter in vowel:
            new_word.append(vowel)
    return new_word


# # Identify the data type of the following values

# In[2]:


type(99.9)


# In[3]:


type('false')


# In[4]:


False


# In[5]:


type('0')


# In[6]:


type (0)


# In[7]:


True


# In[8]:


type('True')


# In[9]:


type([{}])


# In[10]:


type({'a' : []})


# # What data type would best represent?

# str - A term or phrase typed into a search box?

# bool - If a user is logged in?

# float - A discount amount to apply to a user's shopping cart?
#         ie 10% (0.10)

# bool - Whether or not a coupon is valid?

# str - An email address typed in to registration form

# float - The price of a product ($--.--)

# List - A matrix?

# List - The email addresses collected from a registion  
#        form?

# Dictionary - Information about applicants to Codeup's 
#              data science program?

# In[11]:


'1' + 2


# In[ ]:


6 % 4


# In[ ]:


type(6 % 4)


# In[ ]:


type(type(6 % 4))


# In[ ]:


'3 + 4 is ' + 3 + 4


# In[ ]:


0 < 0


# In[ ]:


'False' == False


# In[ ]:


True == 'True'


# In[ ]:


5 >= -5


# In[ ]:


get_ipython().system('False or False')


# In[ ]:


True or "42"


# In[ ]:


get_ipython().system('True && !False')


# In[ ]:


6 % 5


# In[ ]:


5 < 4 and 1 == 1


# In[ ]:


'codeup' == 'codeup' and 'codeup' == 'Codeup'


# In[ ]:


4 >= 0 and 1 !== '1'


# In[ ]:


6 % 3 == 0


# In[ ]:


5 % 2 != 0


# In[ ]:


[1] + 2


# In[ ]:


[1] + [2]


# In[ ]:


[1] * 2


# In[ ]:


[1] * [2]


# In[ ]:


[] + [] == []


# In[ ]:


{} + {}


# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

# In[ ]:


m = 3
b = 5
h = 1
cost =((m*3)+(b*3)+(h*3))
print(cost)


# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

# In[ ]:


g = 400
a = 380
f = 350

week_pay = ((g * 6) + (a * 4) + (f * 10))
print (week_pay)


# Question:
# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

# Answer:
# student == student.class if class_size <= Max and 
# student.class != student.schedule.class.current

# Question:
# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

# Answer:
# 
# If member == premium and offer.date <= offer.expirationdate
# then offer == discount
# 
# Else
# offer == (product * 2) and offer.date <= offer.expirationdate

# # Use the following code to follow the instructions below:

# In[43]:


username = 'codeup'
password = 'notastrongpassword'


# In[13]:


if len(password) > 5:
    print(True) 
else:
    print(False)


# In[14]:


if len(password) > 5 and len(username) <= 20:
    print(True) 
else:
    print(False)


# In[15]:


if len(password) > 5 and len(username) <= 20 and username != password:
    print(True) 
else:
    print(False)


# In[44]:


#Bonus

if len(password) > 5 and len(username) <= 20 and username != password and username == username.strip() and password == password.strip():
    print(True) 
else:
    print(False)


# In[29]:



a = " houseforsale "
a.lstrip()
print (len(a))

b = "houseforsale"
b.lstrip()
print (len(b))
a == a.strip()


# # 17 list comprehension problems in python

# In[1]:


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


# In[3]:


#  Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

[fruit.upper() for fruit in fruits]


# In[4]:


# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

[fruit.capitalize() for fruit in fruits]


# In[8]:


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels
for i in fruits:
    count = (i.count("a"))+(i.count("e"))+(i.count("i"))+(i.count("o"))+(i.count("u"))
    if count > 2:
        list(i)
        print (i)
        
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if(
    fruit.count("a") +
    fruit.count("e") +
    fruit.count("i") +
    fruit.count("o") +
    fruit.count("u") >2
)]

print(fruits_with_more_than_two_vowels)


# In[9]:


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

fruits_with_only_two_vowels = [fruit for fruit in fruits if(
    fruit.count("a") +
    fruit.count("e") +
    fruit.count("i") +
    fruit.count("o") +
    fruit.count("u") == 2
)]

print(fruits_with_only_two_vowels)


# In[11]:


# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
for i in fruits:
    count = len(i)
    if count > 5:
        list(i)
        print (i)
        
[fruit for fruit in fruits if(
    len(fruit) > 5
)]


# In[14]:


# Exercise 6 - make a list that contains each fruit with exactly 5 characters

for i in fruits:
    count = len(i)
    if count == 5:
        list(i)
        print(i)
        
[fruit for fruit in fruits if(
    len(fruit) == 5
)]  


# In[16]:


# Exercise 7 - Make a list that contains fruits that have less than 5 characters

for i in fruits:
    count = len(i)
    if count < 5:
        list(i)
        print(i)
        
[fruit for fruit in fruits if(
    len(fruit) < 5
)]  


# In[17]:


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

[len(i) for i in fruits]
    


# In[22]:


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = [fruit for fruit in fruits if(
"a" in fruit
)]

print(fruits_with_letter_a)


# In[26]:


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers

even_numbers = [number for number in numbers if(
number % 2 == 0
)]

print(even_numbers)


# In[27]:


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

odd_numbers = [number for number in numbers if(
number % 2 != 0
)]

print(odd_numbers)


# In[29]:


numbers == even_numbers + odd_numbers


# In[80]:


type(even_numbers)


# In[30]:


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

positive_numbers = [number for number in numbers if(
number > 0
)]

print(positive_numbers)


# In[31]:


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

negative_numbers = [number for number in numbers if (
number < 0
)]

print(negative_numbers )


# In[78]:


numbers == positive_numbers + negative_numbers


# In[79]:


type(positive_numbers)


# In[34]:


print(len(numbers))
print(len(positive_numbers))
print(len(negative_numbers))


# In[83]:


A = (len(numbers))
B = (len(positive_numbers))
C = (len(negative_numbers))

A == B + C


# In[84]:


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

[number for number in numbers if len(str(abs(number))) > 1 ]
    


# In[85]:


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

[number ** 2 for number in numbers]


# In[86]:


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

[number for number in numbers if number < 0 and number % 2 == 1]


# In[90]:


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

[number + 5 for number in numbers]


# In[ ]:




