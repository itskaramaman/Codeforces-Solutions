q=int(input())
for i in range(q):
    x,y=map(int,input().split())
    if x!=y:
        a=1
        if x>y:
            b=y-1
            c=x-y-1
        else:
            b=x-1
            c=y-x-1    
        
    else:
        a=x-1
        b=1
        c=1       
    print(str(a)+" "+str(b)+" "+str(c))    