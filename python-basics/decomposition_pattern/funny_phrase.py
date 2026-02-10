"""

Write a function `funny_phrase` that accepts a sentence string.

The function should return the sentence where **every other word** has its vowels repeated **twice consecutively**.

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


def funny_phrase(sentence):
    new_sentence = sentence.split()
    new_list =[]
    for i in range(len(new_sentence)):

        if i % 2 == 0:
            new_list.append(new_sentence[i])
        else:
            new_word = double_vowel(new_sentence[i])
            new_list.append(new_word)

    return " ".join(new_list)








print(funny_phrase("she dreamed of being a runner"))
# 'she dreeaameed of beeiing a ruunneer'

print(funny_phrase("park near the stoplight"))
# 'park neeaar the stoopliight'

print(funny_phrase("we need many gardeners"))
# 'we neeeed many gaardeeneers'

