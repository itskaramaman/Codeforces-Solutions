a,b,c,d=map(int,input().split())
timer=0

z=[a,b,c]
z.sort()
mid=z[1]

if mid-z[0]<d:
    timer=timer+(d-(mid-z[0]))
if z[2]-mid<d:
    timer=timer+(d-(z[2]-mid))


print(timer)
