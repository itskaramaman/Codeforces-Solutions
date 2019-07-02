n=int(input())
hand=list(map(int,input().split()))
pile=list(map(int,input().split()))

def handEmpty(x):
    for i in x:
        if i!=0:
            return True
    return False

count=0
while handEmpty(hand):
    for i in hand:
        if i!=0:
            x=i
            hand[hand.index(i)]=pile[0]
            count=count+1
            break

    pile.append(x)
    pile.remove(pile[0])

for i in range(len(pile)-1):
    if pile[i]<pile[i+1]:
        pile[i],pile[i+1]=pile[i+1],pile[i]
        count+=1
    
print(pile)
print(count)