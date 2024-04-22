class Employee:
    def __init__(self,salary):
        self.salary=salary
    def __gt__(self,other):
        if self.salary>other.salary:
            print('Employee 1 has greater salary')
        else:
            print('Employee 2 has greater salary')
    def __lt__(self,other):
        if self.salary<other.salary:
            print('Employee 1 has less salary')
        else:
            print('Employee 2 has less salary')        
e1=Employee(15000)
e2=Employee(30000)
e1>e2
e1<e2