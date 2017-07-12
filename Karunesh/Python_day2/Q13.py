import re
lam=raw_input("Enter alphabet")
if (bool(re.search(r'[aeiou]',lam))):
    print "Vowel"
else: print"Consonant"
        
