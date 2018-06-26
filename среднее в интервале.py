a=int(input())
b=int(input())
k=0
s=0
sred=0
for i in range(a,b):
    if i%3==0:
        s+=i;
        k+=1
print(s/k)
