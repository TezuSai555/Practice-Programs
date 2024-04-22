x=int(input("enter start number:"))
y=int(input("enter end number:"))
for i in range(1,y+1):
    n=3**i
    if n in range(x,y+1):
        print(n)
    elif n<x:
        continue
    else:
        break