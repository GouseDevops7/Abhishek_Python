# print all occured numbers in a string

import re

str = "16 june is sun in 2024 "
pattern = r"\d+"

check = re.findall(pattern,str)

if check:
    print("yes str has number and all occured numbers are :",check)

else:
    print("No  str has no number")