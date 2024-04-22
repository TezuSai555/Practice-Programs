letter=input("Enter a char ")[0]
print(ord(letter))
if letter.islower():
    small=ord(letter)-32
    print(chr(small))
else:
    cap=ord(letter)+32
    print(chr(cap))