list=[0,1,2,3,4,5,6,7,8,9]

l1=[]
l2=[]

for n in list:
    if(n%2==0):
        l1.append(n)
    else:
        l2.append(n)
print("Even",l1)
print("Odd",l2)
    