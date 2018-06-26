# put your python code here
##list=[int(i) for i in input().split()]
list=[1,3,5,6,10]
z=[]
counts=len(list)
if len(list)==1:
    print(list[0])
else:
    for i in range(0, len(list)):
        if i==0:
            z.append(list[i+1]+list[-1])
        elif i==counts-1:
            z.append(list[0]+list[-2])
        else:
            z.append(list[i+1]+list[i-1])
print(z)            







