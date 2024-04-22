num=int(input("Enter a Number"))
flag=False
if num>1:
    for i in range(2,num):
        if num%i==0:
            flag=True
            break
else:
    print("1 is not Prime Number")
if flag == False:
    print("Prime")
else:
    print("Not Prime")