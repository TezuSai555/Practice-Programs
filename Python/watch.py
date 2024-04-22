import time
num=int(input('Enter time in seconds:'))
for i in range(num,-1,-1):
    seconds=i%60
    minutes=(i//60)%60
    hours=i//3600
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(i)
print('Finish!👍')