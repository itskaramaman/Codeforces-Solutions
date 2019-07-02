x=list(input())
d={}
for i in x:
	if i not in d:
		d[i]=1
	else:
		d[i]+=1


if d['(']==d[')'] and d['{']==d['}'] and d['[']==d[']']:
	print('balanced')
else:
	print('unbalanced')			