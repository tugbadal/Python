def fact(n):
    carpim=1
    while(n>0):
        carpim*=n
        n-=1
    return carpim
        
def kombinasyon(n,r):
    return fact(n)/(fact(n-r)*fact(r))



