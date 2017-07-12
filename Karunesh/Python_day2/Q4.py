b=1
i=0
a=[1,1]
a=map(int,a)
while(b<=50):
    b=b+a[i]
    i=i+1
    a.append(b)
if a[len(a)-1]>50: a.pop()
print a
    
