number = int(raw_input("no."))
flag=True
while(number!=1 and flag==True):
    if number%2==0:
        number=number/2
        
    else:
        flag=False
if flag==True:
    print "Yes"
else: print "NO"
