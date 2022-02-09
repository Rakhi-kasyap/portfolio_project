def add():
    a=[2,-7,5,-64,-14]
    i=0
    c=0
    c1=0
    while i<len(a):
        if a[i]<0:
            c+=1
        else:
            c1=1
        i=i+1
    print('negative',c)
    print('positive',c1)
add()