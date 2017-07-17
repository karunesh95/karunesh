import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')


t = raw_input("If C to F:C else F.Choose")
a=int(raw_input("no.?"))
if t=="C":
   print (" The temp in Feh is %dF"%(a*1.8+32))
elif t=="F":
    print("The temp in Cel is %dC"%(a*(5/9)-(32*5/9)))

