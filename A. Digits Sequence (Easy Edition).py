s=""
k=int(input())
i=1
while len(s)<=k:
    s=s+str(i)
    i+=1
print(s[k-1])    