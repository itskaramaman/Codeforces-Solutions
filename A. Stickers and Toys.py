T=int(input())
for i in range(T):
    n,s,t=map(int,input().split())
    print(n-min([s,t])+1)