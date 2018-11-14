# author: Valery Mosyagin
# регулярные выражения

import re


def test1():
    # find numbers
    text = "lkejrfl49 ljfnekr123erf   115 "
    # text = "dsdfsfsfd"    
    match = re.findall("\d+",text)    
    print(match[0] if match else 'Not found')     
    print(match)

def test2():
    # replace
    text = "ljweofitestlefiitestkjweftestkjlf"
    res = re.sub("test","-TEST-",text)
    print("res=", res)
    

test1()
test2()