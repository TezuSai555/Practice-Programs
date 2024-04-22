binary=input("enter a binary form:")  #101
decimal=0
for i in binary:  #1  0  1
    decimal=decimal*2+int(i)  #0*2+1=1,  #1*2+0=2,  #2*2+1=5
print(f'The decimal form of {binary} is:{decimal}') 