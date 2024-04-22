num=int(input('Enter a number'))                                                            
temp=num    
sum=0
while num!=0:
    fact=1
    r=num%10
    for i in range(1,r+1):
        fact=fact*i
    sum+=fact
    num//=10
if sum==temp:
    print("Strong Number")
else:
    print("Not Strong Number")