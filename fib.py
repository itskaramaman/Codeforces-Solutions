def fib(n,d={}):
    if n in d:
        return d[n]
    if n==0 or n==1:
        f=n
    else:
        f=fib(n-1)+fib(n-2)   
        d[n]=f     
    return f

print(fib(8))    