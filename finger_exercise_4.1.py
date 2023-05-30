"""
Finger exercise 11: Write a function isIn that accepts two strings as
arguments and returns True if either string occurs anywhere in the other,
and False otherwise. Hint: you might want to use the built-in str
operation in.
"""
# Solution 1

# def is_In(str1, str2):
#     if len(str1) > len(str2): # Comparing which string is longer and checking to see
#         if str2 in str1:      # if the shorter string is present in the longer string 
#             return True
#     else:
#         if str1 in str2:
#             return True
#     return False

# test = is_In('abc','abcdef')
# print(test)

# Solution 2

# def isIn(string1, string2):
#     return bool(string1 in string2 or string2 in string1)

# word1 = 'abc'
# word2 = 'def'

# test = isIn(word1, word2)

# print(test)



str1 = input('Enter word 1: ')
str2 = input('Enter word 2: ')

def isIn(str1, str2):
    return bool(str1 in str2 or str2 in str1)

test = isIn(str1, str2)

print(test)