lam=int(raw_input("No.?"))
print len(str(lam))
a=0
for i in range(len(str(lam))):
    a=a+int(lam%10)
    lam=int(lam/10)
print("a="+str(a))

    

