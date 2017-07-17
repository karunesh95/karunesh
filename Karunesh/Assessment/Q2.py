lam=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lines=int(raw_input("Enter the no. of lines to print"))
m=0
print "yes"
for i in range(lines):
    for j in range(i+1):
        if j==i:
            print str(lam[m])
            m=m+1
        else:
            print str(lam[m]),
            m=m+1


        
        
        
        
    
