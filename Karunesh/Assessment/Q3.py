tot= int(raw_input("Tot nos. of tuples in List"))
L=[]
for i in range(tot):
    print "Enter the Tuple no. "+str(i+1)
    numbers = raw_input("").split(",")
    
    L.append(tuple(numbers))
print L
def MyFn(a):
    return a[1]
print sorted(L, key=MyFn)
