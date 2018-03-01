largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    
    if num == "done":
        break
    else:
        try:
            num = int(num)
            if num > largest:
              largest = num
            elif smallest is None or num < smallest:
              smallest = num
        except:
            print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest