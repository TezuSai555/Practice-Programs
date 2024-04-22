def fib(n):
    n1,n2=0,1
    for i in range(1,n+1):
        n3=n1+n2
        print(n1,end=' ')
        n1=n2
        n2=n3
fib(5)