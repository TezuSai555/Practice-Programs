num=int(input('Enter a Number'))
temp=num
result=0
flag=False
while num!=0:
    r=num%10
    result=(result*10)+r
    num//=10
for i in range(2,result):
    if result%i==0:
        flag=True
if flag==False:
    print('Prime Palindrome')
else:
    print('Not Prime Palindrome')
#2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 383, 727, 757, 787, 797, 919, 929, 10301, 10501, 10601, 11311