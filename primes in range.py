a=14
#x=int(input('Num1:'))
#y=int(input('Num2:'))

def f2(a):
    count=0
    for x in range(a+1):
        if myfunc(x)==2:
            count+=1
        else:
            pass
    return count

def myfunc(x):
    z=0
    for i in range(1,x+1):
        if x%i==0:
            z+=1
        else:
            pass
    return z

print(f2(a))
