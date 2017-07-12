m=int(raw_input("Row?"))
n=int(raw_input("Column?"))

if m>=3 and n>=3:
    for i in range(m):
        if i==0:
            print "*"*(n-1)
        elif i>0 and i<int(m-1): print "*"+" "*(n-2)+"*"
        elif i==m-1: print "*"*(n-1)
else: print "Cant Print D for this size"
