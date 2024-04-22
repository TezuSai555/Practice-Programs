import numpy as np
arr=np.array([[20,30,40,30],[70,50,60,80]])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.reshape(2,4))
demo1=np.where(arr>30)
print(demo1)
demo=arr>50
print(demo)
arr.sort()
print(arr)