year=int(input('Enter a Year: '))
if year%4==0 and year%100!=0:
    print('Leap Year')
else:
    print('Non Year')