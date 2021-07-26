def sumdigit(n):
    sum=0
    while n>0:
        r=n%10
        if r%2!=0:
            sum=sum+r
        n=n//10
    print(sum)
# sumdigit(2321456)           
# 2321456,6,0
# 232145,5,5
# 23214,4,5
# 2321,1,6
# 232,2,6
# 23,3,9
# 2,2,9
# 0


