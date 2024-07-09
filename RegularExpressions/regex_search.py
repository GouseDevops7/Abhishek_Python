# print first occured number in the string.

import re
str = " 16 june is sun in 2024"
pattern = r"\d+"

check = re.search(pattern,str)

if check:
    print("yes str has number and first coccured number is:",check.group())

else:
    print("No  str has no number")