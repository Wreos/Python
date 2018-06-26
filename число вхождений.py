genom=input()
p=(genom.count("c") + genom.count("g")+genom.count("G") + genom.count("C"))
z=(p/len(genom)) * 100
print(z)
