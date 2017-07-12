m=int(raw_input("Row?"))
n=int(raw_input("Column?"))

if m>=4 and n>=4:
    for i in range(m):
        if i==0:
            print " "+"*"*(n-2)
        elif i>0 and i<int(m/2):
            if i==1: print "*"+" "*(n-2)
            else: print "*"
        elif i==int(m/2): print"*"+" "*1 +"*"*(n-2)
        elif i>int(m/2) and i<m-1: print "*"+" "*(n-2)+"*"
        elif i==m-1: print " "+"*"*(n-2)
else: print "Cant Print G for This size"
