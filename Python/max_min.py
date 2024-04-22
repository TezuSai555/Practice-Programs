demo=[10,20,30,120,50]
min=demo[0]
max=demo[0]
for i in demo:
    if min>i:
        min=i
    elif max<i:
        max=i
print(f'min={min}')
print(f'max={max}')