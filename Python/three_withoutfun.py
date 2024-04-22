x=int(input('Enter starting Number'))
y=int(input('Enter ending Number'))
p=[]
for i in range(x,y+1):
    z=3**i
    p.append(z)
for j in range(x,y):
    if j in p:
        print(j,end=' ')
print(p)