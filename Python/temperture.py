temp=float(input('Enter temperture'))
if temp>0:
    faren=(temp*9/5)+32
    print('Converted temperture in fahrenheit=',faren)
elif temp<0:
    kelvin=temp+273.5
    print('Converted temperture in kelvin=',kelvin)
else:
    print('Entered temperture is equal to o\u00b0c')
