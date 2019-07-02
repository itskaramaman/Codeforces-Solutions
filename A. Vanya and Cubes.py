a=int(input())
n=1
count=0
while a>=((n*(n+1))//2):
    a=a-((n*(n+1))//2)
    count+=1
    n=n+1
print(count)