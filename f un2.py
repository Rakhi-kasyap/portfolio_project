# def fun():
#     a=["i am anjali"]
#     i=0
#     while i<len(a):
#         b=a[i].split()
#         print(b)
#         i=i+1
# fun()


a=int(input("enter a number"))
if a%3!=0 and a%5!=0:
    print("fizzbuzz")
elif a%3!=0:
    print("fizz")
elif a%5!=0:
    print("buzz")
elif a%11!=0:
    print("22")