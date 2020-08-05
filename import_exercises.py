

#     1. Import and test 3 of the functions from your functions exercise file.
#        Import each function in a different way:
#         - import the module and refer to the function with the . syntax
#         - use from to import the function directly
#         - use from and give the function a different name

x = -5
import math
math.fabs(x)

x = [2,3,4,5]
import statistics as s
s.mean(x)

from time import ctime as ct
ct()


#     2. For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
#           - How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
#           - How many different ways can you combine two of the letters from "abcd"?




#     3. Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, 
#        it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
#       #     - Total number of users
        #     - Number of active users
        #     - Number of inactive users
        #     - Grand total of balances for all users
        #     - Average balance per user
        #     - User with the lowest balance
        #     - User with the highest balance
        #     - Most common favorite fruit
        #     - Least most common favorite fruit
        #     - Total number of unread messages for all users
