# Based on numbers split it

import re

text = "I have 2 apples and 3 oranges"
pattern = r"\d+"

result = re.split(pattern, text)
print(result)