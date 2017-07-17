st=raw_input("Write the string here")
from collections import Counter
L=st.split()

M=set(L)
A=[]

A=[(str(Counter(L).keys()[i]),str(Counter(L).values()[i])) for i in range(len(M))]
def MyFn(a):
    return a[0].lower()
A=sorted(A, key=MyFn)
for i in range(len(M)):
    print A[i][0],":",A[i][1]
