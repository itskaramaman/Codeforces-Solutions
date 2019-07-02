a=input()

def sumOFNumber(x):
    return sum(list(map(int,list(a))))

while sumOFNumber(a)%4!=0:
    a=str(int(a)+1)
print(a)    
