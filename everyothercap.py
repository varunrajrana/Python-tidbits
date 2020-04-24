x='Anthropomorphism'
def myfunc(x):
    x1=x.lower()
    x2=x.upper()
    y=''
    for i in range(len(x)):
        if i%2==0:
            y+=x1[i]
        else:
            y+=x2[i]
    return(y)

print(myfunc(x))

myfunc(x)
