import numpy as np
mat1=np.matrix([[1,4,3],[6,8,7],[3,5,7]])
mat2=np.matrix([[4,6,3],[2,8,5],[2,8,4]])
print(mat1)
print(mat2)
print(np.dot(mat1,mat2))
print(np.transpose(mat1))
print(np.trace(mat2))
print(np.add(mat1,mat2))
print(mat1-mat2)