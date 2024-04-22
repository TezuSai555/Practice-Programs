import sys
sys.setrecursionlimit(200)
print(sys.getrecursionlimit())
i=1
def demo():
    global i
    print('Hello',i)
    i+=1
    demo()
demo()