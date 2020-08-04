
______________________________________________________________________________________ 
 # 1. Define a function named is_two. It should accept one input and return True 
    #    if the passed input is either the number or the string 2, False otherwise.
______________________________________________________________________________________
# is_two defines a single parameter (x), which can be a string, int, or float. It will return the boolean value True or False 
def is_two(x):
# check to see if the passed argument is in set of values
    if x in (
        2, 
        2.0, 
        "two", 
        "TWO", 
        "Two",
        "TWo",
        "TwO",
        "tWO",
        "2"):
# if passed argument is in set return True
        return True
# if passed argument is not in set return False     
    else:
        return False

is_two("cheese")
is_two(2)
is_two(2.0)
is_two(2.1)
is_two("two")
is_two("tWO")
assert type(is_two(2)) == bool
______________________________________________________________________________________
# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, 
#    False otherwise.
______________________________________________________________________________________
# is_vowel defines a single parameter (i), which is a string. It will return a boolean value True or False
def is_vowel(i):
# check to see if passed argument type matches assertion test   
    assert type(i) == str, "Invalid Input"
# vowels is a variable that is associated with a string that includes all the vowels
    vowels = "aeiouAEIOU"
# i iterates through the string associated with the variable named vowels
    if i in vowels:
# if i matches any of the letters in the string associated with the variable vowel, is_vowel returns True
        return True
# if i does not match any of the letters in the string associated with the variable vowel, is_vowel returns False
    else:
        return False

is_vowel("a")
is_vowel("E")
is_vowel(2)
is_vowel("Apple")
______________________________________________________________________________________
    # 3. Define a function named is_consonant. 
    #    It should return True if the passed string is a consonant, False otherwise. 
    #    Use your is_vowel function to accomplish this.
______________________________________________________________________________________

# is_consonant defines a single parameter (i), which is a string.  It will return a boolean value True or False
def is_consonant(i):
# I am calling the previous function is_vowel to validate the parameter(i) 
    if is_vowel(i) == False:
# if is_vowel is False, is_consonant will return True        
       return True
# if is_vowel is True, is_consonant will return False
    else:
        return False

is_consonant("a")
is_consonant("E")
is_consonant(2)
is_consonant("Apple")
is_consonant("c")
is_consonant("z")
______________________________________________________________________________________
    # 4. Define a function that accepts a string that is a word. The function should capitalize 
    #    the first letter of the word
    #    if the word starts with a consonant.
______________________________________________________________________________________
def capitalize (word):
    assert type(word) == str, "Invalid Input"
    splitstring = word.split()
    for letter in splitstring:
        if is_consonant(letter[0]):
            return word.capitalize()
        else:
            return word

capitalize("house")
capitalize(3)
capitalize("acre")
capitalize(4.5)
______________________________________________________________________________________
    # 5. Define a function named calculate_tip. It should accept a tip percentage 
    #    (a number between 0 and 1) and the bill total, and return the amount to tip.
______________________________________________________________________________________

def calculate_tip(tip_percent, bill):
    assert type(tip_percent) == int or type(tip_percent) == float, "Invalid Input"
    assert type(bill) == float, "Invalid Input"
    tip = bill * tip_percent
    return print(f" You should tip ${tip}")


calculate_tip("orange", 2)
calculate_tip(2, "orange")
calculate_tip(0, 35.00)
calculate_tip(0.20, 35.00)
calculate_tip(0.05, 35.00)

______________________________________________________________________________________
    # 6. Define a function named apply_discount. It should accept a original price, 
    #    and a discount percentage, and return the price after the discount is applied.
______________________________________________________________________________________

def apply_discount(original_price, discount_percent):
    assert type(original_price) == int or type(original_price) == float, "Invalid Input"
    assert type(discount_percent) == float, "Invalid Input"
    discount_amount = original_price * discount_percent
    final_price = original_price - discount_amount
    return print(f"The price after discount is\n ${final_price}")

apply_discount("orange", 2)
apply_discount(2, "orange")
apply_discount(25.00, .03)
apply_discount(25, 0.75)
apply_discount(3, 1)
______________________________________________________________________________________

    # 7. Define a function named handle_commas. It should accept a string that is a number 
    #    that contains commas in it as input, and return a number as output.
______________________________________________________________________________________

def handle_commas(number_with_comma):
    assert type(number_with_comma) == str, "Invalid Input"
    for char in number_with_comma:
        if char == ",":
            number_with_comma = number_with_comma.replace(char, "")
    return float(number_with_comma)


handle_commas(2)
handle_commas("2,0")
handle_commas("2,000")
______________________________________________________________________________________

    # 8. Define a function named get_letter_grade. It should accept a number and return 
    #    the letter grade associated with that number (A-F).
# Grade Ranges:

#     A : 100 - 88
#     B : 87 - 80
#     C : 79 - 67
#     D : 66 - 60
#     F : 59 - 0
______________________________________________________________________________________

    def get_letter_grade(number):
        assert type(number) == int or type(number) == float, "Invalid Input"
        if number >= 88:
            return print(" That score is associated with the letter grade 'A'")

        elif number >= 80 and number < 88:
            return print(" That score is associated with the letter grade 'B'")

        elif number >= 67 and number < 80:
            return print(" That score is associated with the letter grade 'C'")

        elif number >= 60 and number < 67:
            return print(" That score is associated with the letter grade 'D'")
        else:
            return print(" That score is associated with the letter grade 'F'")
        
get_letter_grade(78)
get_letter_grade(56.8)
get_letter_grade(94.4)
get_letter_grade(60)
______________________________________________________________________________________

    # 9. Define a function named remove_vowels that accepts a string and returns a string 
    #    with all the vowels removed.
______________________________________________________________________________________

def remove_vowels (word):
    assert type(word) == str, "Invalid Input"
    vowels = ("a", "e", "i", "o", "u")
    for letter in word:
        if letter in vowels:
            word = word.replace(letter, "")
    return word

remove_vowels (34)
remove_vowels ("Pineapple")
remove_vowels ("Superman")
remove_vowels ("ardvark")
______________________________________________________________________________________

    # 10. Define a function named normalize_name. It should accept a string and return a 
    #     valid python identifier, that is:
    #     - anything that is not a valid python identifier should be removed
    #     - leading and trailing whitespace should be removed
    #     - everything should be lowercase
    #     - spaces should be replaced with underscores
    #     - for example:
    #         Name will become name
    #         First Name will become first_name
    #         % Completed will become completed

______________________________________________________________________________________

def normalize_name(text):
    assert type(text) == str, "Invalid Input"
    new_string = (text.strip("0123456789 ").lower().replace(" ", "_"))   
    output = ""                                                     
    for i in new_string:
        if i not in "!@#$%^&*()+=-[]{}\/|?.<>,`~":                    
            output += i                                              
    return(output)


normalize_name("    bye   ")
normalize_name("Name")
normalize_name("First Name")
normalize_name("% Completed")

hi = "hello world"
hi = hi.replace(" ", "_")
print(hi)

______________________________________________________________________________________
    # 11. Write a function named cumulative_sum that accepts a list of numbers 
    #     and returns a list that is the cumulative sum of the numbers in the list.
    #     cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    #     cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
______________________________________________________________________________________

def cumulative_sum(lists):  
    assert type(lists) == list, "Invalid Input"
    cu_list = []  
    length = len(lists)  
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]  
    return cu_list[1:] 


cumulative_sum([1, 1, 1]) 
cumulative_sum([1, 2, 3, 4])
______________________________________________________________________________________


