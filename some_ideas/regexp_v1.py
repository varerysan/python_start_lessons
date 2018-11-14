# author: Valery Mosyagin
# регулярные выражения

import re


def test1():
    text = "lkejrfl49 ljfnekr123erf   115 "
    # text = "dsdfsfsfd"    
    match = re.findall("\d+",text)    
    print(match[0] if match else 'Not found')     
    print(match)

test1()