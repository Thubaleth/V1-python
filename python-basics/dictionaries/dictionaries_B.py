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

#====================================================================================
"""
Write a function `most_common_letter` that accepts a string as an argument.

The function should return the character that appears **most frequently** in the string.

You may assume:

- There are **no ties**
- The string contains only lowercase letters

"""

def most_common_letter(str):
    max_letter = ""
    max_num = 0


    for ch in str:
        count = str.count(ch)
        if count > max_num:
            max_num = count
            max_letter = ch
        
    return max_letter

    

print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'

#=================================================================================================
"""
Write a function `word_replace` that accepts:

- a sentence string
- a dictionary

The function should return a new sentence where words that appear as keys in the dictionary are replaced with their corresponding values.
"""

def  word_replace(sentence,dict):
    new_sentence = sentence.split()
    new_list = []
    for word in new_sentence:

        if word in dict:
            new_list.append(dict[word])
        
        else:
            new_list.append(word)
        
    return " ".join(new_list)

    




print(word_replace(
"I never take naps during the day",
    {"never":"always","day":"weekend" }
))
# 'I always take naps during the weekend'

print(word_replace(
"the park is closed",
    {"closed":"open","the":"a" }
))
# 'a park is open'

print(word_replace(
"I do what I want",
    {"I":"we","cat":"dog" }
))
# 'we do what we want'

