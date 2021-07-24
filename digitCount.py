def digitcount(n):
    n=abs(n)
    c=0
    if(n==0):
        return 1
    else:
        while (n>0):
            n//=10
            c+=1
        return c