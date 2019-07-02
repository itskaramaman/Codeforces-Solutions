import math
points=[(-2,4),(0,-2),(-1,0),(3,5),(-2,-3),(3,2)]
d={} #using dictionary 
for point in points:
	d[point]=math.sqrt( (point[0]**2) +(point[1]**2) )



#sorting dictionary by value
d=sorted(d.items(), key= lambda x:x[1])

#taking user input
k=int(input())
#printing k points
for i in range(k):
	print(d[i][0])



