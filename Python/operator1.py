class Student:
    def __init__(self,c1,c2):
        self.m1=c1
        self.m2=c2
    def __add__(self,other):
        marks1=self.m1+other.m1
        marks2=self.m2+other.m2
        return Student(marks1,marks2)
s1=Student(50,60)
s2=Student(70,80)
s3=s1+s2
print(s3.m1)