
text = ['abc', 'aabaa', '245235', '123321']

t2 = text[::-1]

print("t2=", t2)

pal = [s for s in text if s == s[::-1] ]

print("pal=", pal)