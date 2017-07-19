r=int(raw_input("How many transactions???"))
import re
B=[]
S=0
for i in range(r):
    B.append(raw_input("Enter"+str(i)+":"))
for i in B:
    if i[0]=="D":
        S=S+int(re.findall(r'\d+', i)[0])

    if i[0]=="W":
        S=S-int(re.findall(r'\d+', i)[0])
print S
