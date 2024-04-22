#def greet(a,b):
#    c=a+b
#    return c
#print(greet(10,20))
#def person(name,age):
#    print('name:',name)
#    print('age:',age)
#person(name='kamal',age=23)
def person(name,*data):
    print('name:',name)
    print('data',data)
person('rani',23,35000,'dev')
#def person1(name,**data):
#    print('name:',name)
#    #print('data',data)
#    for i,j in data.items():
#        print(i,j)
#person1('rajesh',age=21,sal=35000,department='dev')
