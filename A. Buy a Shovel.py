k,r=map(int,input().split())
count=1
z=[r,0]
while (k*count)%10 not in z:
    count=count+1
print(count)