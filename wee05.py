# Intersection of two strings
def instersection(foo:str, bar:str) -> str | None:
    # this makes an empty string where we can store characters found both in foo and bar
    result = "" 
    # a loop that itereates through each character of the first string 
    for character in foo:
        # iterates through the second string and checks if the character is also there
        # simultaneously checks if the character isn't already in result so that there aren't any duplicates
        if character in bar and character not in result:
            # adds the character to result
            result += character
    # if a result is found it is returned as a string but if it's still empty None is returned
    return result if result else None
# Calls the intersection function
print(instersection)  

# Alphabetical assessment
def is_alphabetical(string:str) -> bool:
    # we assume that the string only has letters in it
    only_letters = True
    # then we loop through each character in the string
    for character in string:
        # and we get the ASCII value of the character
        ascii_code = ord(character)
        # checks if the chracters ASCII code is not a letter
        if not (65 <= ascii_code <= 90 or 97 <= ascii_code <= 122):
            only_letters = False 
    # returns if all characters were letters if not, False
    return only_letters 
# Calls the is_alphabetical function
print(is_alphabetical)

# Letters only
def letters_only(string:str) -> str | None:
    # I made an empty string to collect letters
    letters = ""
    # iterate through each character 
    for character in string:
        # gets each characters ascii value and checks if its a letter
        ascii_code = ord(character)
        if (65 <= ascii_code <= 90 or 97 <= ascii_code <= 122):
            # adds each letter to letters
            letters += character
    # returns the result and if it's not a letter returns None
    return letters if letters else None 
# Calls the function letters_only
print(letters_only) 

# Palindrom generator
def generate_palindrome(string:str) -> str | None: 
    # creates a variable palindrom setting it to None
    # None will be returned unless there actually is an input string
    palindrome = None
    # this checks if the input string is empty
    if string != "":
        # set a variable to store the reversed input
        reversed_string = ""
        # variable i is set to keep track of what chracter we're on in 
        i = len(string) - 1
        while i >= 0:
            reversed_string += string[i]
            i -= 1
        palindrome = string + reversed_string
    return palindrome
print(generate_palindrome)





#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))
