pal=input()
i=0
j=len(pal)-1
is_palindrom=True
while i<j:
    if pal[i]!=pal[j]:
        is_palindrom=False
        print("Не палиндром")
        break;
    i+=1
    j-=1
else:
        print("yes")
