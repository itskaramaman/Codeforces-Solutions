n=int(input())
x=list(map(int,list(input())))
     
countZero=len(list(filter(lambda a: a==0,x)))
countOne=n-(countZero)


print(abs(countZero-countOne))
    