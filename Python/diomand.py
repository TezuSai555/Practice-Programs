num=int(input('Enter Number of Rows:'))
for i in range(1,num):
    for j in range(1,num-i+1):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()
for i in range(num,0,-1):
    for j in range(1,num-i+1):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()