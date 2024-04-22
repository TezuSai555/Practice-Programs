class Hello:
    def demo1(self):
        print('This is from parent class')
class Demo(Hello):
    def demo1(self):
        super().demo1()
        print('This is from child class')
d=Demo()
d.demo1()