# Replace string digits by 9

import re

text = "I have  7 apples and 12 oranges"
pattern = r"\d+"
replace_with = "9"

check_text_has_number = re.search(pattern, text)

if(check_text_has_number == None):
     print("text has no numbers")
else:
     result = re.sub(pattern, replace_with, text)
     print("Numbers in the text were replaced by 9 and the final output is:", result)
     

