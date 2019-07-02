def hcf(x, y):  
   if x > y:  
       smaller = y  
   else:  
       smaller = x  
   for i in range(1,smaller + 1):  
       if((x % i == 0) and (y % i == 0)):  
           hcf = i  
   return hcf  

a,b,n=map(int,input().split())
winner=1
while n>0:
    if winner%2!=0:
        n=n-hcf(n,a)
    else:
        n=n-hcf(n,b)
    winner=winner+1

if winner%2!=0:
    print(1)
else:
    print(0)    