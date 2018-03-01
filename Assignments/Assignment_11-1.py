import re

name = raw_input("Enter file:")
if len(name) < 1: 
    name = "regex_sum_42.txt"
handle = open(name)

total = 0
for line in handle:
    nums = re.findall('[0-9]+', line)
    if len(nums) > 0:
        for num in nums:
            total = total + int(num)
print total