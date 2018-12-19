# Search or filter words
words = ["арбуз","корова","ананас","стол","швабра","алмаз", "банка"]

res = []
for w in words:
    if w.startswith(("а", "б")):
        res.append(w)

print("res=", res)


res2 = [w for w in words if w.endswith("з")]

print("res2=", res2)
        

words_data = []
with open("words.txt","r", encoding="utf-8") as file:
    for line in file.readlines():
        words_data += line.split()
 
print("words_data=", words_data)

res3 = [w for w in words_data if w.startswith("к")]
print("res3=", res3)

res4 = [w for w in words_data if w.lower().startswith("к")]
print("res4=", res4)
