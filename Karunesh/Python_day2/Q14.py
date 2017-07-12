year=int(raw_input("Year"))
month=int(raw_input("Month"))
day=int(raw_input("Day"))
if month<13 and day<32:
    print (" The next date is[%d-%d-%d]"%(year,month,day+1))
else: "Wrong Date input"
