n=int(input())
h=map(int,input().split())
i=h.index(1)
j=h.index(n)
if j>i and j-i%2==0:
	energy=h[j]-h[i]
print(energy)
