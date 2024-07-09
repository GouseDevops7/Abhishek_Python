# match: check string start with it or not
# match.group() : returns matching part

#Find out given string start with  a number or not? if it starts with number then return the number

import re
str = "2023 year"
pattern = r"\d+" # It mean don't conside back slashes like\n,\t.. and start with number [0-9]

check = re.match(pattern, str)

if check:
    print("yes string start with a number and matching number is:", check.group())
else:
    print("String not tarted with number")