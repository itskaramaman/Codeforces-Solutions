n,m=map(int,input().split())
flag=False

if n%2==0:
    moves=n//2
else:
    moves=(n-1)//2+1

while moves<=n:
    if moves%m==0:
        flag=True
        break
    else:
        moves=moves+1 

if flag==True:
    print(moves)
else:
    print(-1)               





