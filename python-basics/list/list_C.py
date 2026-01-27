# Write a function `lengthiest_word(sentence)` that accepts a string containing a sentence.
# The function should return the longest word in the sentence.
# If there is a tie, return the word that appears later in the sentence.

# Example:
# lengthiest_word("I am pretty hungry") -> 'hungry'
# lengthiest_word("we should think outside of the box") -> 'outside'
# lengthiest_word("down the rabbit hole") -> 'rabbit'
# lengthiest_word("simmer down") -> 'simmer'

def lengthiest_word(sentence):

    arr_sentence = sentence.split()
    longest = arr_sentence[0]
    
    for word in arr_sentence:

        if len(word) >= len(longest):
            longest = word

    return longest

print(  lengthiest_word("down the rabbit hole")    )
      

#==============================================================================================
# Write a function `alternating_caps(sentence)` that accepts a string containing a sentence.
# The function should return the sentence where words alternate between lowercase and uppercase.

# Example:
# alternating_caps("take them to school") -> 'take THEM to SCHOOL'
# alternating_caps("What did ThEy EAT before?") -> 'what DID they EAT before?'


          