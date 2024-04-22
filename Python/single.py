#class demo:
#    college='kbn'
#    @classmethod
#    def stu(cls):
#        return cls.college
#    @staticmethod
#    def add(a,b):
#        return a+b
#print(demo.add(10,20))
#print(demo.stu())
class Parent:
    def hello(self):
        print('This is from parent class')
class child(Parent):
    def demo(self):
        print('This is from child1')
c=child()
c.demo()
class child2(child):
    def demo1(self):
        print('This from child2')
c1=child2()
c1.hello()


class A:
    def demo1(self):
        print('This is from A')
class B:
    def demo1(self):
        print('This is from B')
class C(A,B):
    def dummy(self):
        print('This is from C')
c=C()
c.demo1()
B.demo1(c)