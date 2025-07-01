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

# Palindrome generator
def generate_palindrome(string:str) -> str | None: 
    # creates a variable palindrom setting it to None
    # None will be returned unless there actually is an input string
    palindrome = None
    # this checks if the input string is empty
    if string != "":
        # set a variable to store the reversed input
        reversed_string = ""
        # variable i is set to keep track of what chracter we're on in the string
        # len(string) - 1 gives use the index of the last character of the string
        i = len(string) - 1
        # this loop will run as long as i is greater than or equal to 0
        # strating from the last character and move bacwards to the first
        while i >= 0:
            # the character at position i in the string gets added to reversed_string
            reversed_string += string[i]
            # after adding a character 1 is subtracted from i to move back a character in teh string
            i -= 1
        # once all characters have been reversed it takes the original string and adds its reversed version onto it
        palindrome = string + reversed_string
    # this returns the palindrome of the inputted string
    return palindrome
# Calls the generate_palindrom function
print(generate_palindrome)

# Palindrome detector
def is_palindrome(string:str) -> bool:
    # thris creates an empty string named final whereonly lowercase letters and digits will be stored
    final = "" 
    # a loop that itirates through the string in the input
    for character in string:
        asc_code = ord(character)
        # once we have the ascii code for the characters it checks if they are letters or digits
        if (65 <= asc_code <= 90 or 97 <= asc_code <= 122 or 48 <= asc_code <= 57):
            # this is so that no uppercase letters are in teh string, converting them to lowercase
            if 65 <= asc_code <= 90:
                # takes chr() so that it takes the ascii code and returns the characters it represents 
                character = chr(asc_code + 32)
            final += character
    reversed_final = "" #reverses final form of the string
    # variable i is set to keep track of what chracter we're on in the string
    # len(string) - 1 gives use the index of the last character of the string
    i = len(final) - 1
     # this loop will run as long as i is greater than or equal to 0
     # strating from the last character and move bacwards to the first
    while i >= 0:
        # the character at position i in the string gets added to reversed_string
        reversed_final += final[i]
        # after adding a character 1 is subtracted from i to move back a character in teh string
        i -= 1
    # return True if "final" equals its reversed form "reversed_final", if not it returns False
    return final == reversed_final
# Calls the is_palindrome function
print(is_palindrome)




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
