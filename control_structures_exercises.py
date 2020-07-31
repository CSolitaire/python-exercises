

# 1.Conditional Basics

# Prompt the user for a day of the week, print out whether the day is Monday or not

response = input("What day of the week is today?")
if response.lower().strip() == "monday":
    print ("It is Monday")
else:
    print("Too bad it's not Monday...")
print("Thank You!, Have a nice day!")
   

# Prompt the user for a day of the week, print out whether the day is a weekday or a weekend
response = input("What day of the week is today?")
if response.lower().strip() in weekday:
    weekday = ("monday","tuesday","wednesday","thursday","friday")
    print ("Boo! It is a weekday...")
else:
    print ("Yee Haw! It's the weekend, party time!")


#  Create variables and make up values for
#  - the number of hours worked in one week
#  - the hourly rate
#  - how much the week's paycheck will be
#  Write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours



