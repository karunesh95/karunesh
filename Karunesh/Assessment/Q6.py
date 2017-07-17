em=raw_input("Enter your email>>")
x=""
flag=True
for i in em:
    if (i!='@') and flag==True:
        x=x+str(i)
    else: flag=False
print x
