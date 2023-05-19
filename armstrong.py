# Armstrong 153 1cube+5cube+3cube
#  1+125+27=153
# 407   371   370
def armstrong(n):
    sum=0
    while(n>0):
        a=int(n%10)
        n=int(n/10)
        sum=int(sum+a*a*a)
    print(sum)

    if(m==sum):
        print("Armstrong")
    else:
        print("NOt armstrong")


m=int(input("Enter a number "))
armstrong(m)