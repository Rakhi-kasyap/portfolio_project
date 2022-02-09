
def harshad():
    a=int(input("enter any number"))
    b=asum=0
    while b!=0:
        c=b%10
        sum=sum+c
        b=int(b//10)
    if a%sum==0:
        print("harshad number")
harshad()