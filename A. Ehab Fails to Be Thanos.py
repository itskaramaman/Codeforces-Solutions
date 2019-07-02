n=int(input())
x=list(map(int,input().split()))
x.sort()

if sum(x[:n])!=sum(x[n:]) :
    print(" ".join(map(str,x)))
else:
    print(-1)    