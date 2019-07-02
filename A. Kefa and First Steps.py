n=int(input())
a=list(map(int,input().split()))
i=0
if len(a)==1:
    print(1)
    exit()
maxLength=[]
while i<len(a)-1:
    length=0
    while i<len(a)-1 and a[i]<=a[i+1]:
        length=length+1
        i=i+1
        #print('inner loop '+str(length))
    maxLength.append(length)
    i=i+1
    #print('outer loop '+str(i))


print(max(maxLength)+1)