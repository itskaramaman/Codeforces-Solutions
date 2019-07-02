n=int(input())
countm=0
countc=0
for i in range(n):
    m,c=map(int,input().split())
    if m>c:
        countm+=1
    elif c>m:
        countc+=1
if countc<countm:
    print('Mishka')    
elif countc>countm:
    print('Chris')  
else:
    print('Friendship is magic!^^')    