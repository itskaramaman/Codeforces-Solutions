a=int(input())
x=list(map(int,input().split()))
taxi=0
z={}
for i in x:
	if i not in z:
		z[i]=1
	else:
		z[i]+=1

taxi=z[4]+z[3]+z[2]/2
z[1]-=z[3]

if z[2]%2==1:
	taxi=taxi+1
if z[1]>0:
	taxi=(z[1]+3)/4

print(taxi)


#{1: 1, 2: 1, 3: 1, 4: 2}