"""
Write a function `double_vowel` that accepts a string as an argument.

The function should return a new string where **every vowel** in the original string is repeated **twice consecutively**.

Vowels are: `a, e, i, o, u`
"""

def double_vowel(str):
    new_str = ""
    for ch in str:
        if ch in "aeiou":
            new_str += ch *2
        else:
            new_str += ch

    return new_str 




print(double_vowel("runner"))
# 'ruunneer'

print(double_vowel("stoplight"))
# 'stoopliight'

print(double_vowel("gardener"))
# 'gaardeeneer'


