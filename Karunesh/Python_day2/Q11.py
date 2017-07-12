m=int(raw_input("Row?"))
n=int(raw_input("Column?"))

if m>=4 and n>=4 and n%2!=0:
    if m%2==0:
        for i in range(m):
            if i==0: print "*"+" "*(n-2)+"*"
            if i>0 and i<int(m/2): print "*"+" "*(i-1)+"*"+" "*((n-2)-2*i)+"*"+" "*(i-1)+"*"
            elif i==int(m/2): print"*"+" "*((n-3)/2)+"*"+" "*((n-3)/2)+"*"
            elif i>int(m/2): print "*"+" "*(n-2)+"*"
    else:
        for i in range(m):
            if i==0: print "*"+" "*(n-2)+"*"
            if i>0 and i<int(m/2): print "*"+" "*(i)+"*"+" "*((n-4)-2*i)+"*"+" "*(i)+"*"
            elif i==int(m/2): print"*"+" "*((n-3)/2)+"*"+" "*((n-3)/2)+"*"
            elif i>int(m/2): print "*"+" "*(n-2)+"*"
        


else: print "Cant Print M for This size"
