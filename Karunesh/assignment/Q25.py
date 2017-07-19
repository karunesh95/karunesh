str=raw_input("Enter the string")
B=''
flag=True
for i in str:
    if i=="@":
        flag=False
    if i==".":
        break
    if flag==False and i!="@":
        B=B+i
print B
    
        
