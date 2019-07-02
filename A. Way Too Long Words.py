n=int(input())
for i in range(n):
	x=input()
	if len(x)>10:
		print(x[0]+str(len(x)-2)+x[len(i)-1])
	else:
		print(x)	