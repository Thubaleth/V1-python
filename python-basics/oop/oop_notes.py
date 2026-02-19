class student:
    def __init__(self,name,age,marks):#self is referring to the student object
        self.name = name
        self.age = age
        self.marks = marks
        print("how many times this will run when S1 or s2 is create") #
    
    def result(self):
        print(f'the result is {self.marks}')

s1= student("Thubalethu",27,78)
s2 = student("rob",35,8)

print(s1.name)
print(s2.age)

s3 = student("john",9,90)
s3.result()
