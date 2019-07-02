#x=list(input())
#s=""

#for i in x:
#	if i.isupper():
#		s=s+i
#print(s)		

def capRecusrsive(s,id=0):
	if s[id].isupper():
		return s[id]
	if id==len(s)-1:
		return "No upper letter found"	
	return capRecusrsive(s,id=id+1)	

print(capRecusrsive('hEElO'))

