filename=raw_input("Enter file name: ")
st=raw_input("Write the string here")
f = open(filename, 'a')
f.write("\n"+st)
f.close()

"""
for line in (list(open(filename))):
    print"A"
    print(line.rstrip())
"""
