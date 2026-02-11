# Write a function `pick_prefix(strings, prefix)` that accepts:
# - a list of strings
# - a prefix string
#
# The function should return a list of words that begin with the prefix.

def pick_prefix(strings, prefix):
    new_list = []
    for str in strings:
      
      if str[0:len(prefix)] in prefix:
         new_list.append(str)
      
    return new_list 

print(pick_prefix(['connect','company','concert','cram'],'con'))
# ['connect', 'concert']

print(pick_prefix(['miner','mistake','misspeak','moose','mission'],'mis'))
# ['mistake', 'misspeak', 'mission']

