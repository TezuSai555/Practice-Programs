num=int(input('Enter a number'))
temp=num
count=0
while num!=0:
    count+=1
    num//=10
num=temp
result=0
while num!=0:
    r=num%10
    result+=r**count
    num//=10
if temp==result:
    print('Armstrong')
else:
    print('Not Armstrong')