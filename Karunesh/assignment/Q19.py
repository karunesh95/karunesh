import collections
str=raw_input("Enter string:")
A=[]
for i in str:
    A.append(i)
for i in set(A):
    print i+",",
    print A.count(i)  
    
