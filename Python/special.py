n1=int(input('Enter starting range'))
n2=int(input('Enter ending range'))
for i in range(n1,n2+1):
    digit=[]
    temp=i
    while i!=0:
        r=i%10
        digit.append(r)
        i//=10
    #print(digit)
    if 0 not in digit:
        if temp%digit[0]==0 and temp%digit[1]==0:
            print(temp,end=' ')