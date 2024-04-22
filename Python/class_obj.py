class Student:
    college='KBN'
    def __init__(self,id,name,branch):
        self.id=id
        self.name=name
        self.branch=branch
    def details(self):
        print(f'id={self.id}')
        print(f'Name={self.name}')
        print(f'Branch={self.branch}')
        print(f'College={Student.college}')
#s1=Student()
#s1.id=101
#s1.name='Kamal'
#s1.branch='BCA'
#s1.details()
s2=Student(102,'Rajesh','DS')
s2.details()
s3=Student(103,'Rani','BCA')
s3.details()