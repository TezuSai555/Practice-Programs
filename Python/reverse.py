num=int(input("Enter a Number"))
result=0
while num!=0:
    r=num%10
    result=(result*10)+r
    num//=10
print(result)