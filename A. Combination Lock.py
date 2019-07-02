n=int(input())
a=list(map(int,list(input())))
b=list(map(int,list(input())))
moves=0

for i in range(n):
    clockwise=abs(a[i]-b[i])
    counterClockwise=abs(9-max([ a[i],b[i] ]) + min([ a[i],b[i] ]) +1 )
    if clockwise<=counterClockwise:
        moves=moves+clockwise
    else:
        moves=moves+counterClockwise


print(moves)






