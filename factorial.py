def fact(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    print("factorial of ",n," is ",a)

n=int(input("Enter the number: "))
fact(n)
