

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








