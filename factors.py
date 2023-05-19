def factor(n):
    fact=[]
    for i in range(1,n):
        if(n%i==0):
            fact.append(i)
    
    print("factorial of",n,"are",fact)

a=int(input("Enter a number "))
factor(a)