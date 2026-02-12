# Write a function `trendy_text` that accepts a sentence string as an argument.
# The function should return the sentence where the last vowel of every word
# is removed.
def remove_last_vowel(str):

    for i in range(len(str)-1,-1,-1):
        
        if str[i] in "aeiou":
            first_word = str[0:i]
            second_word = str[i+1:]
            return first_word + second_word
        
    return str

def trendy_text(sentence): 
    

    list_sentence = sentence.split()
    new_list =[]
    for i in list_sentence:
        new_list.append(remove_last_vowel(i))
    
    return " ".join(new_list)




print(trendy_text("the concert will be epic"))
# 'th concrt wll be epc'

print(trendy_text("breakfast food is wonderful"))
# 'breakfst fod s wonderfl'

print(trendy_text("the weather will improve hopefully"))
# 'th weathr wll improv hopeflly'

