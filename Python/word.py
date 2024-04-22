letter=input("Enter a String ")
for i in letter:
    if i.islower():
        small=ord(i)-32
        print(chr(small),end='')
    elif i.isupper():
        cap=ord(i)+32
        print(chr(cap),end='')
    else:
        print(i,end='')