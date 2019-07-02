n=int(input())
s=list(input())
m=int(input())

sdict=dict()
for i in s:
    if i not in sdict:
        sdict[i]=1
    else:
        sdict[i]+=1
print(sdict)
for i in range(m):
    count=0
    x=list(input())
    x=list(set(x))
    print(x)
    for i in x:
        count=count+sdict[i]
    print(count)    


