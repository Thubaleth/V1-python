#Write a function `character_count` that accepts a string as an argument.

#The function should return a **dictionary** containing the count of each character in the string.

def character_count(str):
    
    dict = {}

    for ch in str:
        if ch in dict:
            dict[ch] +=1
        else:
            dict[ch] = 1
    
    return dict






print(character_count("evening"))
# { 'e': 2, 'v': 1, 'n': 2, 'i': 1, 'g': 1 }

print(character_count("mississippi"))
# { 'm': 1, 'i': 4, 's': 4, 'p': 2 }

print(character_count("chili"))
# { 'c': 1, 'h': 1, 'i': 2, 'l': 1 }

#=====================================================================================
"""
Write a function `letter_map` that accepts:

- a string
- a dictionary

The function should return a new string where characters that appear as keys in the dictionary are replaced with their corresponding values.
"""

def letter_map(string,dict):
  new_str = ""

  for ch in string:
      
       if ch in dict:
           new_str += dict[ch]
       else:
           new_str += ch
        
  return new_str
           


print(letter_map("symbolic", {"y":"i","o":"a","c":"k" }))
# 'simbalik'

print(letter_map("colossal", {"o":"x","s":"p" }))
# 'cxlxppal'

print(letter_map("miniscule", {"u":"t","i":"f","e":"q" }))
# 'mfnfsctlq'

