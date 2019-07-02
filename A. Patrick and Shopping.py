houseToShop1,houseToShop2,shop1ToShop2=map(int,input().split())
distance=[]

distance.append(houseToShop1+shop1ToShop2+houseToShop2)
distance.append(houseToShop1+shop1ToShop2+shop1ToShop2+houseToShop1)
distance.append(houseToShop2+houseToShop2+houseToShop1+houseToShop1)
distance.append(houseToShop2+shop1ToShop2+shop1ToShop2+houseToShop2)  

print(min(distance))


