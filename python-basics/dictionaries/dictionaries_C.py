"""
Write a function `greatest_population` that accepts a **list of dictionaries**, where each dictionary represents a country.

Each country dictionary contains:

- `name`
- `population`
- `gdp`

The function should return the **name of the country with the largest population**.

You may assume:

- The list contains **at least one country**
"""

def greatest_population(list_dict):
    population = 0
    max_population = ""
    for country in list_dict:
        

            if country["population"] > population:
                max_population = country["name"]
                population =  country["population"]

    
    
    return max_population
                
    
    
countries1 = [
    {"name":"Cameroon","population":27744989,"gdp":38.68 },
    {"name":"Belarus","population":9477918,"gdp":59.66 },
    {"name":"Indonesia","population":267026366,"gdp":1042 },
    {"name":"Guyana","population":750204,"gdp":3.88 },
]

print(greatest_population(countries1))
# 'Indonesia'



countries2 = [
    {"name":"New Zealand","population":4925477,"gdp":204.9 },
    {"name":"Mozambique","population":30098197,"gdp":14.72 },
    {"name":"Greenland","population":57616,"gdp":2.71 },
    {"name":"Kazakhstan","population":19091949,"gdp":179.3 },
    {"name":"Burma","population":56590071,"gdp":71.21 },
]

print(greatest_population(countries2))
# 'Burma'

#=========================================================================================
"""
Write a function `pluck` that accepts:

- a dictionary
- a list of strings

The function should return a **new dictionary** containing only the key–value pairs where:

- the key exists in the provided list
"""
def pluck(old_dict,str_list):
     
     dict = {}

     for word in str_list:
        for key,value in old_dict.items():
          if key in str_list:
               dict[key] = value

     return dict
     

print(pluck(
    {"name":"Fido","color":"Brown","breed":"German Shepherd" },
    ["name","breed"]
))
# { "name": "Fido", "breed": "German Shepherd" }

print(pluck(
    {"make":"Tesla","mpg":93,"model":"Model X","color":"white" },
    ["make","model"]
))
# { "make": "Tesla", "model": "Model X" }

#==================================================================================
"""

Write a function `object_add` that accepts **two dictionaries** containing numeric values.

Rules:

- If a key appears in **both dictionaries**, sum their values
- If a key appears in **only one dictionary**, keep its value as-is
- Return a **new dictionary**
"""

def object_add(dict_1,dict_2):
    add = 0
    for key,value in dict_1:

        if key in dict_2:
            pass



obj1 = {"x":3,"y":10 }
obj2 = {"y":2,"x":1 }

print(object_add(obj1, obj2))
# { "x": 4, "y": 12 }


obj3 = {"a":3,"b":2,"c": -1 }
obj4 = {"b":5,"c":1,"e":4 }

print(object_add(obj3, obj4))
# { "a": 3, "b": 7, "c": 0, "e": 4 }

