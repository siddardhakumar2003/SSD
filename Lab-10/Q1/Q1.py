n=int(input("Enter a positive integer: "))
for i in range(1,n+1):
    if i<=0:
        print("")
    elif i%3==0 and i%5==0:
        print("ThreeFive")
    elif i%3==0:
        print("Three")
    elif i%5==0:
        print("Five")
    else:
        print(i)
