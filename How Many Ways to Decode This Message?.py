dict={'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z'}

data='123'

def num_ways(x):
	total=0
	if int(x)<=10:
		total=total+1
		print('data is '+x)	
	elif int(x)>10 and int(x)<=26:
		total=total+2	
	elif len(x)==2 and int(x)>26 and int(x)<100:
		total=total+1
	elif len(x)>=3 and int(x[0:2])<=26:
		total=num_ways(x[:2]) + num_ways(x[2:])
	elif len(x)>=3 and int(x[0:2])>26:
		total=num_ways(x[0])+num_ways(x[1:])
	return total

print(num_ways('167'))				

#167 => afg pg 
