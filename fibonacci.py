def fib(n):
    result=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    print(result)

n=int(input("Enter the range "))
fib(n)

