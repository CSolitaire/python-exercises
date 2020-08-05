

#     1. Import and test 3 of the functions from your functions exercise file.
#        Import each function in a different way:
#         - import the module and refer to the function with the . syntax
#         - use from to import the function directly
#         - use from and give the function a different name

import function_exercises
function_exercises.is_two(2)

import function_exercises as fe
fe.is_vowel('a')

from function_exercises import is_consonant as c
c('a')

#     2. For the following exercises, read about and use the itertools module from the 
#        standard library to help you solve the problem.
#           - How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
#           - How many different ways can you combine two of the letters from "abcd"?

#  - How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

from itertools import *
abc = list(product('abc', '123'))
print(abc)

# - How many different ways can you combine two of the letters from "abcd"?

from itertools import * # import itertools
print(list(permutations('abcd', 2))) #Repeated sets, unique locations in set
print(list(combinations('abcd', 2))) #unique sets of values, unique locations in set

#     3. Save this file as profiles.json inside of your exercises directory. 
#        Use the load function from the json module to open this file, 
#        it will produce a list of dictionaries. Using this data, write some code 
#        that calculates and outputs the following information:


import json
with open('profiles.json') as f:
        data = json.load(f)

[x for x in data]
#     - Total number of users

def total_users():
        return len([i['_id'] for i in data])

total_users()
        

#     - Number of active users

def active_users():
        return len([i['_id'] for i in data if i['isActive'] == True])

active_users()

#     - Number of inactive users

def inactive_users():
        return len([i['_id'] for i in data if i['isActive'] == False])

inactive_users()

#     - Grand total of balances for all users

def total_balance():
        total = 0
        for i in data:
                total += float(i['balance'].replace(",", '').replace("$", ""))  
        return total

total_balance()

#     - Average balance per user

def ave_total_all_user():
        return total_balance() / total_users()

ave_total_all_user()

def ave_total_active_user():
        return total_balance() / active_users()

ave_total_active_user()

#     - User with the lowest balance
def lowest_balance():
        balance = min([i['balance'] for x in data])
        name = [i['name'] for i in data if i['balance'] == min([i['balance'] for i in data])]
        return print(f"{name} has the lowest account balance with {balance}")

lowest_balance()

 #     - User with the highest balance
 def highest_balance():
        balance = min([i['balance'] for x in data])
        name = [i['name'] for i in data if i['balance'] == max([i['balance'] for i in data])]
        print(f"{name} has the highest account balance with {balance}")

highest_balance()

#     - Most common favorite fruit

[i['favoriteFruit'] for i in data] #shows me the fruit in the dataset, there are only 3 fruits identified

def fav_fruit():
        s = 0        
        b = 0
        a = 0
        for x in data:
                if i['favoriteFruit'] == 'strawberry':  
                        s += 1
                if i['favoriteFruit'] == 'banana':
                        b += 1
                if i['favoriteFruit'] == 'apple':
                        a += 1
        fruits = [{'fruit' : 'strawberry', 'count' : s}, {'fruit' : 'banana', 'count' : b}, {'fruit' : 'apple', 'count' : a}]   
        total_count = (max([i['count'] for i in fruits]), max([i['fruit'] for i in fruits]))  
        return total_count

fav_fruit()

#     - Least most common favorite fruit

def least_fav_fruit():
        s = 0        
        b = 0
        a = 0
        for x in data:
                if i['favoriteFruit'] == 'strawberry':  
                        s += 1
                if i['favoriteFruit'] == 'banana':
                        b += 1
                if i['favoriteFruit'] == 'apple':
                        a += 1
        fruits = [{'fruit' : 'strawberry', 'count' : s}, {'fruit' : 'banana', 'count' : b}, {'fruit' : 'apple', 'count' : a}]   
        total_count = (min([i['count'] for i in fruits]), min([i['fruit'] for i in fruits]))  
        return total_count

least_fav_fruit()

#     - Total number of unread messages for all users

def total_unread():
        unread_m = [int(i["greeting"].lower().strip("abcdefghijklmonpqrstuvwxyz!,. ")) for i in data if "unread" in i["greeting"]] 
        total_m = sum(unread_m)
        return print(f"there are a total of {total_m} unread messages") 

total_unread()
