n=int(input("Enter a number"))
m=0
for i in range(2,n-1):
    if(n%i==0):
        m=m+1

if(m==0):
    print("is Prime")
else:
    print("Not prime")
    