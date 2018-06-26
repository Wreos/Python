# put your python code here
a=int(input())
b=int(input())
m=a*b
while (a!=0) and (b!=0):
    if a>b:
        a %= b
    else:
        b %= a
nod=m//(a+b)
print(nod)
