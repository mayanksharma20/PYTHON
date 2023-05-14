list=[0,4,5,6,7,8,9,10,11,15,17]

prime=[]
notprime=[]
for n in (list):
    flag=0
    if(n==0 or n==1):
        notprime.append(n)
    else:
        for i in range(2,n):
            if(n%i==0):
                flag=1
                break
        
        if(flag==0):
            prime.append(n)
        else:
            notprime.append(n)

print("Prime",prime)
print("Not a prime",notprime)