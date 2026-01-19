def sum_of_range(n):
    sum = 0
    for i in range(n+1):
        sum += i
    
    print(sum)
        
   

sum_of_range(5)
# prints: 15

#===================================================================
#Write `countdown(start)`

#Print from start → 1.

def countdown(start):
    for i in range(start, 0, -1):
       print(i)

countdown(5)


#=================================================================

#find_char_positions("banana", "a")
# 1
# 3
# 5


def find_char_positions(str, char):
    print(str.lower().count(char))

find_char_positions("banana", "n")


#=================================================================

#multiplication_table(4)
# 4
# 8
# 12
# ...
# 40

def multiplication_table(number):
    
    for i in range(1,11):
        print(i*number)

multiplication_table(4)



