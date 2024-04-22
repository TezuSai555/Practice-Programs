def series(n):
    if n<=1:
        return n
    return(series(n-1)+series(n-2))
n=int(input('Enter a Number'))
for i in range(n):
    print(series(i),end=' ')