# Write a function `lala_language` that accepts a sentence string as an argument.
# The function should return a new sentence where words longer than 3 characters
# are modified.
#
# Modified words should have each vowel followed by 'l' and the same vowel again.
# See the examples below.

def lala_language(sentence):
    new_sentence = sentence.split()
    new_list = []
    vowels = "aeiou"
    
    for word in new_sentence:
        new_word = ""

        if len(word) > 3:
            for ch in word:
                if ch in vowels:
                    new_word += ch + "l" +  ch
                else:
                    new_word += ch
            else:
             new_list.append(new_word)
        else:
            new_list.append(word)
    
    return " ".join(new_list)
    
    
    
                
            
    






            


print(lala_language('this is pretty strange'))
# 'thilis is preletty stralangele'

print(lala_language('can you speak our language'))
# 'can you spelealak our lalangulualagele'
