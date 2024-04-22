num=int(input('Enter range of number'))
count=0
for i in range(1,num):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=' ')
            count+=1
print('\n count=',count)