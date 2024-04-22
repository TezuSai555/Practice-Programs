import numpy as np
demo1=np.array([11,23,14,125,15])
demo2=demo1
print(demo1)
print(demo2)
print(id(demo1))
print(id(demo2))
demo3=demo1.view()#shallow copy
demo1[0]=10
print(demo3)
print(id(demo3))
demo4=demo1.copy()#deep copy
demo4[0]=11
print(demo4)
demo1[4]=34
print(demo1)
print(id(demo4))
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])
print(a*b)