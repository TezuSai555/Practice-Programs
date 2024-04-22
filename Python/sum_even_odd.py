n1=int(input('Enter Starting Number'))
n2=int(input('Enter ending Number'))
x=0
y=0
for i in range(n1,n2):
    if i%2==0:
        x+=i
    else:
        y+=i
print(f'Even Sum {x}')
print(f'odd Sum {y}')