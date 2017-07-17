import re
import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')
lam=raw_input("Enter alphabet")
if (bool(re.search(r'[aeiou]',lam))):
    print "Vowel"
else: print"Consonant"
        
