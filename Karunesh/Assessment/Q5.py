numbers = raw_input().split(",")
            
b = [float(x) for x in numbers]
b.sort()
A=b
print "list:"
print A
print "Output:"
for i in range(len(A)):
    if i!=len(A)-1:
        if int(A[i])!=int(A[i+1])+1:
            for j in range(int(A[i])+1,int(A[i+1])):
                print j

