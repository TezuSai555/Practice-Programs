class Demo1:
    def hello(self):
        print('Hello from Demo1')
class Demo2:
    def hello(self):
        print('Hello from Demo2')
def access(obj):
    obj.hello()
d1=Demo1()
d2=Demo2()
access(d1)
access(d2)