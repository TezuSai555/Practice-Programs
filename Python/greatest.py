a=int(input('Enter First Number'))
b=int(input('Enter Second Number'))
c=int(input('Enter Third Number'))
if a>b and a>c:
    print(f'{a} is Greatest')
elif b>c:
    print(f'{b} is Greatest')
else:
    print(f'{c} is Greatest')