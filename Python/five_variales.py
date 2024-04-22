a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
d=int(input("Enter Fourth Number:"))
e=int(input("Enter Fivth Number:"))
if a>b and a>c and a>d and a>e:
    print(f'{a} is Bigger')
elif b>c and b>d and b>e:
    print(f'{b} is Bigger')
elif c>d and c>e:
    print(f'{c} is Bigger')
elif d>e:
    print(f'')