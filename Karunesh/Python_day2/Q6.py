m=int(raw_input("Row?"))
n=int(raw_input("Column?"))

if m>=3 and n>=3:
    for i in range(m):
        if i==0:print " "+"*"*(n-2)
        elif i>0 and i<int(m/2):
            print "*"+" "*(n-2)+"*"
        elif i==int(m/2): print"*"*n
        elif i>int(m/2): print "*"+" "*(n-2)+"*"
else: print "Cant Print A for This size"

