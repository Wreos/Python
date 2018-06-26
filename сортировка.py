##list=[int(i) for i in input().split()]
list=[1,3,2,3,9,8,9]
z=sorted(list)
counts=len(z)
for i in range(0, len(z)):
        if z.count(i)>1:
             print(i, end=' ')
             i=+1
        else:
            i=+1
            continue
