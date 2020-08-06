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


## 20 Python Data Structure Manipulation Exercises

students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

    # How many students are there?

 print(f"There are {len(students)} students")

    # How many students prefer light coffee? 

light_coffee = [student['coffee_preference'] for student in students if student['coffee_preference'] == 'light']

print(f'{len(light_coffee)} students prefer light coffee.')

#     For each type of coffee roast?

light = 0
medium = 0
dark = 0

for i in students:
    if i['coffee_preference'] == "light":
        light += 1
    elif i['coffee_preference'] == "medium":
        medium += 1
    elif i['coffee_preference'] == "dark":
        dark += 1
        
print(f'{light} students prefer light coffee.')
print(f'{medium} students prefer light coffee.')
print(f'{dark} students prefer light coffee.')

    # How many types of each pet are there?

[x['pets'] for x in students]

def student_pets():
    h = 0
    c = 0
    d = 0
    for x in students:
        for items in x['pets']:
            if items['species'] == 'horse':
                h += 1
            if items['species'] == 'cat':
                c += 1
            if items['species'] == 'dog':
                 d += 1
    print(f" The pets found in students include {c} cats, {d} dogs, and {h} horses.")

student_pets()

    # How many grades does each student have? 

for x in students:
    print(x['student'], 'has',len(x['grades']), 'grades')


   # Do they all have the same number of grades?

test = [len(x['grades']) for x in students]

if len(set(test)) != 1:
    print ('not all students have the same number of grades ')
else:
    print('all of the students have the same amount of grades')
   
   
    # What is each student's grade average?

for x in students:
    print(x['student'],'has a grade average of', sum(x['grades']) / (len(x['grades'])))

    # How many pets does each student have?

for x in students:
    print (x['student'], 'has', len(x['pets']), 'pets')

    # How many students are in web development? data science?

wd = 0
ds = 0

for x in students:
    if x['course'] == 'web development':
        wd += 1
    if x['course'] == 'data science':
        ds += 1 

print(f'There are {wd} web development students.')
print(f'There are {ds} data science  students.')

    # What is the average number of pets for students in web development?

wd_count = 0
pet_count = 0

for x in students:
    if x['course'] == 'web development':
        wd_count += 1
        for i in x['pets']:
            pet_count += 1

# len([x for q in students for x in q['pets'] if q['course'] == 'web development'])

# len([x for q in students if q['course'] == 'web development'])

avg_pet_count_wd = round(pet_count / wd_count, 2)

print(avg_pet_count_wd)

    # What is the average pet age for students in data science?


pet_count = 0
pet_age = 0

for stud in students:
    if stud['course'] == 'data science':
        for pet in stud['pets']:
            pet_age += pet['age']
            pet_count += 1
            
# len([x for q in students for x in q['pets'] if q['course'] == 'web development'])

avg_pet_age_ds = round(pet_age / pet_count, 2)

print(avg_pet_age_ds)


    # What is most frequent coffee preference for data science students?

light = 0
medium = 0
dark = 0

for i in students:
    if i['course'] == 'data science':
        if i['coffee_preference'] == "light":
            light += 1
        elif i['coffee_preference'] == "medium":
            medium += 1
        elif i['coffee_preference'] == "dark":
            dark += 1

cc = [{"preference":'light', "votes":light}, {"preference":'medium', "votes":medium}, {"preference":'dark', "votes":dark}]

seq = max([x['votes'] for x in cc])


for x in cc:
    if x['votes'] == seq:
        print(f"{x['preference']} is the most popular coffee preference with {x['votes']}")

    # What is the least frequent coffee preference for web development students?

l = 0
m = 0
d = 0

for x in students:
    if x['course'] == 'web development':
        if x['coffee_preference'] == 'light':
            l += 1
        elif x['coffee_preference'] == 'medium':
            m += 1
        elif x['coffee_preference'] == 'dark':
            d += 1

cc = [{"preference":'light', "votes":l}, {"preference":'medium', "votes":m}, {"preference":'dark', "votes":d}]


seq = [x['votes'] for x in cc]

for x in cc:
    if x['votes'] == min(seq):
        print(f"{x['preference']} is the least favorite coffee preference with only {x['votes']} votes")

    # What is the average grade for students with at least 2 pets?

grades_combined = 0
number_of_grades = 0

for x in students:
    if len([i for i in x['pets']]) > 1:
        grades_combined += sum(x['grades'])
        number_of_grades += len([i for i in x['grades']])

avg_grd_2_pets = round(grades_combined / number_of_grades, 2)

print(avg_grd_2_pets)

    # How many students have 3 pets?

total_students = 0

for x in students:
    if len([i for i in x['pets']]) == 3:
        total_students += 1
    
print(f"{total_students} student(s) has exactly three pets.")

#alternate answer
# print(f"{len([x for x in students if len(x['pets']) == 3])} student(s) have 3 exactly 3 pets ")

    # What is the average grade for students with 0 pets?

grades_combined = 0
number_of_grades = 0

for x in students:
    if len([i for i in x['pets']]) == 0:
        grades_combined += sum(x['grades'])
        number_of_grades += len([i for i in x['grades']])

avg_grade_no_pets = round(grades_combined / number_of_grades , 2)

print(avg_grade_no_pets)

    # What is the average grade for web development students? 
combined_grades = 0
number_of_grades = 0

for x in students:
    if x['course'] == 'web development':
        combined_grades += sum(x['grades'])
        number_of_grades += len([i for i in x['grades']])

avg_grade_wd = round(combined_grades / number_of_grades , 2)

print(avg_grade_wd)


    # data science students?

combined_grades = 0
number_of_grades = 0

for x in students:
    if x['course'] == 'data science':
        combined_grades += sum(x['grades'])
        number_of_grades += len([i for i in x['grades']])

avg_grade_wd = round(combined_grades / number_of_grades , 2)

print(avg_grade_wd)


    # What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?

coll = []

for x in students:
    if x['coffee_preference'] == 'dark':
        coll.append((( sum(x['grades']) / (len([x for x in x['grades']])), x['student'])))

coll.sort(reverse = True)
print(coll)

    # What is the average number of pets for medium coffee drinkers?

pet_count = 0
student_count = 0

for x in students:
    if x['coffee_preference'] == 'medium':
        pet_count += len([i for i in x['pets']])
        student_count += 1
        
avg_pet_count = round(pet_count / student_count , 2)

print(avg_pet_count)

    # What is the most common type of pet for web development students?

horses = 0
cats = 0
dogs = 0

for x in students:
    if x['course'] == 'web development':
        for i in x['pets']:
            if (i['species']) == 'horse':
                horses += 1
            if (i['species']) == 'cat':
                cats += 1
            if (i['species']) == 'dog':
                dogs += 1

animals=[{'pet':'horses', 'amount':horses}, {'pet':'cats', 'amount':cats}, {'pet':'dogs', 'amount':dogs}]

seq = max([x['amount'] for x in animals])

for x in animals:
    if x['amount'] == seq:
        print(f"{x['amount']} {x['pet']} are owned among all WD students, making them the most common pet type.")

    # What is the average name length?

name_lengths_total = 0
total_students = 0

for x in students:
    name_lengths_total += len(x['student'])
    total_students += 1
    
avg_name_length = round(name_lengths_total / total_students, 2)

print(avg_name_length)


    # What is the highest pet age for light coffee drinkers?


oldest_pets = []

ra = 0

for x in students:
    if x['coffee_preference'] == 'light':
        for i in x['pets']:
            if i['age'] >= ra:
                ra = i['age']
                oldest_pets.append((i['age'], i['species']))
        
print(oldest_pets)



