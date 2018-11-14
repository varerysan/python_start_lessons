# author: Valery Mosyagin
# регулярные выражения

import re

text = "lkejrfl49 ljfnekr123erf   115 "

match = re.findall("\d+",text)

print(match[0] if match else 'Not found') 

print(match)
