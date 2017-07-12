'''
import sys
print("a= ")
a=int(sys.argv[1])
print ("b= ")
b=int(sys.argv[2])
print a+b
print a*b
print a/b
print a-b
print a%b
'''
import sys
c=sys.argv[1].lower()
print "Length of Text= "
print len(c)
a=1
L=0
M=len(c)
while(L<(M/2)):
    if c[L]!=c[M-1-L]:
        a=2
    L+=1
print a
if a==2:
    print "Not a Palindrome"
else:
    print "Palindrome"
    



