m=int(raw_input("Row?"))
n=int(raw_input("Column?"))

if m>=3 and n>=3:
    for i in range(m):
        if i<m-1: print "*"
        elif i==m-1: print "*"*(n)
else: print "Cant Print L for This size"
