

# 1.Conditional Basics

# A. Prompt the user for a day of the week, print out whether the day is Monday or not

response = input("What day of the week is today?")
if response.lower().strip() == "monday":
    print ("It is Monday")
else:
    print("Too bad it's not Monday...")
print("Thank You!, Have a nice day!")
   

# B. Prompt the user for a day of the week, print out whether the day is a weekday or a weekend
response = input("What day of the week is today?")
weekday = ("monday","tuesday","wednesday","thursday","friday")
if response.lower().strip() in weekday:
    print ("Boo! It is a weekday...")
else:
    print ("Yee Haw! It's the weekend, party time!")


#  C. Create variables and make up values for
#  - the number of hours worked in one week
#  - the hourly rate
#  - how much the week's paycheck will be
#  Write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hours_worked = 41
hourly_rate = 10.00

if hours_worked <= 40:
    take_home = hours_worked * hourly_rate
    print(f'This week I made ${take_home}.')
else:
    take_home = (hours_worked * hourly_rate) + ((hours_worked - 40) * (hourly_rate + (hourly_rate / 2)))
    print(f'This week I made ${take_home}.')


# 2. Loop Basics

# A. While Loops
#         Create an integer variable i with a value of 5.
#         Create a while loop that runs so long as i is less than or equal to 15
#         Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1

#     . Create a loop that will count by 2's starting with 0 and ending at 100. 
#        Follow each number with a new line.

i = 0
while i <= 100:
  print(i)
  print(" ")
  i += 2

 #    . This code puts a space between the numbers but not a new line 

i = 0
while i <= 100:
  print(i," ",end=" ")
  i += 2
  
#     . Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
  print(i," ")
  print( " ")
  i -= 5

#     . Create a while loop that starts at 2, and displays the number squared 
#        on each line while the number is less than 1,000,000.

i = 2
while i <= 1_000_000:
    print(i)
    i *= i 

#     . Write a loop that uses print to create the output shown below.

i = 105
while i >= 10: i-= 5; print(i)
  

# B.For Loops

#     . Write some code that prompts the user for a number, 
#       then shows a multiplication table up through 10 for that number.



# This changes the user input in to a string, it has to be
# at the begining to work
user_input = str(input("Please type an INT between 0 and 9"))
print (user_input_int)

#Now i need to take that input and iterate through a list
user_input = int(input("Please type an INT between 0 and 9"))
for number in range(10):
    print (user_input * number)

#It iterated but did not save values, now i need a list
user_input = int(input("Please type an INT between 0 and 9"))
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
user_input_results = [user_input * number for number in numbers]

#Now i think I need a formatted string for my answer...
user_input = int(input("Please type an INT between 0 and 9"))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_input_results = [user_input * number for number in numbers]
i = 0
while i >= 10:
    print(f"{user_input} x {numbers[0]} = {user_input_results[0]}")
    i += 1

#Not formatted string, just variables converted back to string
user_input = int(input("Please type an INT between 0 and 9"))
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
user_input_results = [user_input * number for number in numbers]
print((user_input))
print(numbers[0])
print(user_input_results[0])

#Endproduct
user_input = int(input("Please type an INT between 0 and 9"))
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
user_input_results = [user_input * number for number in numbers]
print(str(user_input) + " X " + str(numbers[0]) + " = " + str(user_input_results[0]))
print(str(user_input) + " X " + str(numbers[1]) + " = " + str(user_input_results[1]))
print(str(user_input) + " X " + str(numbers[2]) + " = " + str(user_input_results[2]))
print(str(user_input) + " X " + str(numbers[3]) + " = " + str(user_input_results[3]))
print(str(user_input) + " X " + str(numbers[4]) + " = " + str(user_input_results[4]))
print(str(user_input) + " X " + str(numbers[5]) + " = " + str(user_input_results[5]))
print(str(user_input) + " X " + str(numbers[6]) + " = " + str(user_input_results[6]))
print(str(user_input) + " X " + str(numbers[7]) + " = " + str(user_input_results[7]))
print(str(user_input) + " X " + str(numbers[8]) + " = " + str(user_input_results[8]))
print(str(user_input) + " X " + str(numbers[9]) + " = " + str(user_input_results[9]))
