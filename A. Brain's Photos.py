n,m=map(int,input().split())
z=[]
for i in range(n):
    a=list(input().split())
    z.extend(a)
   
if  'C' in z or 'M' in z or 'Y' in z:
    print('#Color')    
else:
    print('#Black&White')    