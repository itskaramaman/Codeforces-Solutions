n=int(input())
z=[]
flag=False
for i in range(n):
    z.append(input())

for i in z:
    if i[:2]=='OO':
        z[z.index(i)]='++'+i[2:]
        flag=True
        break
    elif i[3:]=='OO':
        z[z.index(i)]=i[:3]+'++'
        flag=True
        break

if flag==True:
    print('YES')
    for i in z:
        print(i)
else:
    print('NO')        



      

