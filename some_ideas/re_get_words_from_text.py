# Author: Valery Mosyagin

import re
text = """Python
Python logo and wordmark.svg
Paradigm	Object-oriented, imperative, functional, procedural, reflective
Designed by	Guido van Rossum
Developer	Python Software Foundation
First appeared	1990; 28 years ago[1]
Stable release	
3.7.1 / 20 October 2018; 41 days ago[2]
2.7.15 / 1 May 2018; 6 months ago[3]
Typing discipline	Duck, dynamic, strong; and since version 3.5: Gradual[4]
License	Python Software Foundation License
Filename extensions	.py, .pyc, .pyd, .pyo (prior to 3.5),[5] .pyw, .pyz (since 3.5)[6]
Website	www.python.org
Major implementations
CPython, IronPython, Jython, MicroPython, Numba, PyPy, Stackless Python
Dialects
Cython, RPython
Influenced by
ABC,[7] ALGOL 68,[8] APL[9] C,[10] C++,[11] CLU,[12] Dylan,[13] Haskell,[14] Icon,[15] Java,[16] Lisp,[17] Modula-3,[11] Perl, Standard ML[9]
Influenced
Boo, Cobra, CoffeeScript,[18] D, F#, Falcon, Genie,[19] Go, Apache Groovy, JavaScript,[20][21] Julia,[22] Nim, Ring,[23] Ruby,[24] Swift[25]
 Python Programming at Wikibooks
Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[26] In July 2018, Van Rossum stepped down as the leader in the language community."""

#print (text)

words = re.findall("\w+", text)
print("--------All words ----------------")
for w in words:
    print("={}=".format(w))
print("----------------------------------")

numbers = re.findall("\d+", text)

print("--------All numbers----------------")
for n in numbers:
    print("={}=".format(n))
print("----------------------------------")

years = re.findall("(?:19|20)\d\d", text)

print("--------All years----------------")
for n in years:
    print("={}=".format(n))
print("----------------------------------")