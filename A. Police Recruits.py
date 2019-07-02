n=int(input())
a=list(map(int,input().split()))
countPolicemen=0
countCrime=0
for i in a:
    if i!=-1:
        countPolicemen+=i
    elif i==-1 and countPolicemen>0:
        countPolicemen-=1
    else:
        countCrime+=1
print(countCrime)            