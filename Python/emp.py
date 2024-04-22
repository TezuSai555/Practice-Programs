class Employee:
    department='HR'
    company='TCS'
    com_Address='Vijayawada'
    def __init__(self,id,name,salary,job_role):
        self.id=id
        self.name=name
        self.salary=salary
        self.job_role=job_role
    def display(self):
        print(f'id={self.id}')
        print(f'Name={self.name}')
        print(f'Salary={self.salary}')
        print(f'Department={Employee.department}')
        print(f'Job_Role={self.job_role}')
        print(f'Company={Employee.company}')
        print(f'Company_Address={Employee.com_Address}')
e1=Employee(101,'Rani',45000,'Assistent')
e1.display()