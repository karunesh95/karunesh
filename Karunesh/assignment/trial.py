lam=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lines=raw_input("Enter the no. of lines to print<8")
m=1
if lines<8:
    for i in range(1,lines+1):
        for j in range(i):
            print (lam[m],end=' ')
            m=m+1
        
        
    
