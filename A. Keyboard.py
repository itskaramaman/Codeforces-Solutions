z=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m',',','.','/']

a=input()
b=list(input())
x=[]
for i in b:
    if a=='R':
        x.append(z[z.index(i)-1])
    else:
        x.append(z[z.index(i)+1])

print("".join(x))           