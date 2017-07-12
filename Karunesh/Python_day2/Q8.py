m=int(raw_input("Row?"))
n=int(raw_input("Column?"))

if m>=4 and n>=4:
    for i in range(m):
        if i==0: print "*"*(n)
        elif i>0 and i<int(m/2):print "*"
        elif i==int(m/2): print"*"*(n)
        elif i>int(m/2) and i<m-1: print "*"
        elif i==m-1: print "*"*(n)
else: print "Cant Print E for This size"
