
    # 1. Define a function named is_two. It should accept one input and return True if the passed input is either 
    #    the number or the string 2, False otherwise.
def is_two(x):
    if x in (2, 2.0, "two", "TWO", "Two"):
        return True
    else:
        return False

is_two("cheese")

is_two(2)

is_two(2.0)

is_two(2.1)

is_two("two")


    # 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(i):
    assert type(i) == str, "Invalid Input"
    vowels = set("aeiouAEIOU")
    if i in vowels:
        return True
    else:
        return False


is_vowel("a")
is_vowel("E")
is_vowel(2)
is_vowel("Apple")

    # 3. Define a function named is_consonant. 
    #    It should return True if the passed string is a consonant, False otherwise. 
    #    Use your is_vowel function to accomplish this.

def is_consonant(i):
    if is_vowel(i) == False:
       return True
    else:
        return False

 
is_consonant("a")
is_consonant("E")
is_consonant(2)
is_consonant("Apple")
is_consonant("c")
is_consonant("z")


    # 4. Define a function that accepts a string that is a word. The function should capitalize 
    #    the first letter of the word
    #    if the word starts with a consonant.

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


    # 5. Define a function named calculate_tip. It should accept a tip percentage 
    #    (a number between 0 and 1) and the bill total, and return the amount to tip.

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


    # 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, 
    #    and return the price after the discount is applied.



    # 7. Define a function named handle_commas. It should accept a string that is a number that contains commas 
    #    in it as input, and return a number as output.



    # 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).



    # 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.



    # 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    #     - anything that is not a valid python identifier should be removed
    #     - leading and trailing whitespace should be removed
    #     - everything should be lowercase
    #     - spaces should be replaced with underscores
    #     - for example:
    #         Name will become name
    #         First Name will become first_name
    #         % Completed will become completed



    # 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
    #     cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    #     cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
