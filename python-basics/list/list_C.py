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








#==========================================================================================
# Write a function `number_range(min_val, max_val, step)` that accepts three numbers as arguments.
# The function should return a list of numbers starting from min_val to max_val (inclusive),
# incremented by step.

# Example:
# number_range(10, 40, 5) -> [10, 15, 20, 25, 30, 35, 40]
# number_range(14, 24, 3) -> [14, 17, 20, 23]
# number_range(8, 35, 6) -> [8, 14, 20, 26, 32]

def number_range(min_val, max_val, step):
     num_list = []
     for number in range(min_val,max_val+1,step):
         num_list.append(number)
    
     return num_list
    
            
print(number_range(14, 24, 3   ) )



#==============================================================================================
# Write a function `remove_short_words(sentence)` that accepts a string containing a sentence.
# The function should return a new sentence where all words shorter than 4 characters are removed.

# Example:
# remove_short_words("knock on the door will you") -> 'knock door will'
# remove_short_words("a terrible plan") -> 'terrible plan'
# remove_short_words("run faster that way") -> 'faster that'

def remove_short_words(sentence):
    new_sentence = sentence.split()
    for word in new_sentence:

        if len(word) < 4:
            new_sentence.remove(word)
    
    return " ".join(new_sentence)

print( remove_short_words("run faster that way") )
        



#+==================================================================================================
# Write a function `common_elements(arr1, arr2)` that accepts two lists as arguments.
# The function should return a new list containing the elements that are found in both input lists.
# The order of elements in the output list doesn't matter.

# Example:
# common_elements(["a", "c", "d", "b"], ["b", "a", "y"]) -> ['a', 'b']
# common_elements([4, 7], [32, 7, 1, 4]) -> [4, 7]


def common_elements(arr1, arr2):
    new_list = []
    for i in arr1:

        for x in arr2:
            if x == i:
                new_list.append(x)
    
    return new_list


print( common_elements([4, 7], [32, 7, 1, 4])  )


    

          