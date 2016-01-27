#ASKS FOR HOURS AND VERIFIES VALUE
stringhrs = raw_input("Enter # of hours: ")
try:
    ihrs = float(stringhrs)
except:
    ihrs = -1
    
#ASKS FOR RATE AND VERIFIES VALUE
if ihrs>=0:
    stringrate = raw_input("Enter pay rate: $")
    try:
        irate = float(stringrate)
    except:
        irate = -1    
#GROSS PAY WITH OT CALCULATED IF ANY        
    if irate>=0:
        if ihrs>40:
            overhrs = ihrs-40
            overrate = irate*1.5
            print "Overtime Pay: $", overrate
            print "Total Gross Pay: $",(40*irate)+(overhrs*overrate)
        elif ihrs<=40:
            print "Total Gross Pay: $",ihrs*irate
    else:
        print "Entry is not a number"
else:
    print "Entry is not a number"
print "Thank you for using my program."   
