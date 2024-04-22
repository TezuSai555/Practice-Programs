num=int(input('Enter a Number'))
temp=num
Result=0
while num!=0:
    r=num%10
    Result=(Result*10)+r
    num//=10
if temp==Result:
    print('Palindrome')
else:
    print('Not Palindrome')