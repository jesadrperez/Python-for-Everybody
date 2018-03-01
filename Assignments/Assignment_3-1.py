hrs = raw_input("Enter Hours:")
hrs = float(hrs)

rate = raw_input("Enter Rate:")
rate = float(rate)

if hrs > 40.0:
    overtime = (hrs - 40) * (1.5*rate)
    regtime = 40* rate
else:
    regtime = hrs * rate
    overtime = 0
    
pay = float(regtime) + float(overtime)
print pay