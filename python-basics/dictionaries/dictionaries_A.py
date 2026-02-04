"""
Write a function `email_parse` that accepts an email address string.

The function should return a dictionary containing:

- `username`
- `domain`
"""
def email_parse(str):

    new_dict = {}
    i = str.find("@")
    username = str[:i]
    domain = str[i+1:]


    new_dict["username"] = username
    new_dict["domain"] = domain
    return new_dict

print(email_parse("coolcoder42@goodmail.com"))
# { 'username': 'coolcoder42', 'domain': 'goodmail.com' }

print(email_parse("az@woohoomail.com"))
# { 'username': 'az', 'domain': 'woohoomail.com' }

print(email_parse("1337pr0graMmer@coldmail.edu"))
# { 'username': '1337pr0graMmer', 'domain': 'coldmail.edu' }

#======================================================================================
"""

Write a function `key_pair` that accepts:

- two dictionaries
- a key string

Return a list containing the values for the given key from both dictionaries.
"""


def key_pair(dict_1,dict_2,str):
    return [dict_1[str],dict_2[str]]

cat1 = {"name":"jinkee","breed":"calico" }
cat2 = {"name":"garfield","breed":"red tabby" }



print(key_pair(cat1, cat2,"breed"))
# ['calico', 'red tabby']

print(key_pair(cat1, cat2,"name"))
# ['jinkee', 'garfield']

#============================================================================

"""
Write a function `element_quantities` that accepts a dictionary where:

- keys are elements
- values are quantities

Return a list containing each element repeated according to its quantity.

"""

def element_quantities(dict):
    lst = []
    for key,value in dict.items():
        for i in range(value):
            lst.append(key)
    
    return lst




quantities1 = {"cat":3,"bird":1,"dog":2 }
print(element_quantities(quantities1))
# ['cat', 'cat', 'cat', 'bird', 'dog', 'dog']

quantities2 = {"blue":3,"brown":1 }
print(element_quantities(quantities2))
# ['blue', 'blue', 'blue', 'brown']


#==============================================================================
"""
Write a function `max_object_value` that accepts a dictionary where:

- keys are strings
- values are numbers

Return a list containing:

- the key with the highest value
- the highest value itself

"""
def max_object_value(dict):
    max_value = 0
    mac_key = ""
    for key,value in dict.items():
        if value > max_value:
            max_value = value
            max_key = key
            
    return[max_key,max_value]

    
        
    
print(max_object_value({"a":5,"b":2,"c":6,"d":7,"e":4 }))
# ['d', 7]

print(max_object_value({"lychee":11,"rambutan":13,"papaya":9 }))
# ['rambutan', 13]
