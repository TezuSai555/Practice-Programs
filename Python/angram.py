str1=input('Enter a String')
str2=input('Enter another String')
rev=""
if len(str1)==len(str2):
    for i in str1:
        rev=i+rev
else:
    print("Given string lengths do not match")
if str2 == rev:
    print("Angram")
else:
    print("Not")

ctrl+shif+P
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser