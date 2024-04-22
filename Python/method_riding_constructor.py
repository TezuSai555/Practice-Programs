#class Hello:
#    def __init__(self):
#        print('Hello from Super class Constructor')
#class Demo(Hello):
#    def __init__(self):
#        super().__init__()
#        print('This is from child class constructor')
#d=Demo()
class Hello:
    def __init__(self):
        self.a=10
        print(self.a)
class Demo(Hello):
    def __init__(self):
        pass
d=Demo()
