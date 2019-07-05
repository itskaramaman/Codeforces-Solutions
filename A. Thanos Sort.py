n=int(input())
a=list(map(int,input().split()))

def recursiveFunction(a,x=[]):
    if a==sorted(a):
        x.append(len(a))
    else:
        z=len(a)//2
        recursiveFunction(a[:z],x)
        recursiveFunction(a[z:],x)
    return max(x)    

print(recursiveFunction(a))