import hashlib

logindata = {"admin": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3", # 123 
             "johh": "5229375c28a89876d931339bf8849af089c2db709c38b894e91521f930fa2e39", # PasS
             "user": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"} #test

username = input("Введите имя пользователя:")
password = input("Введите пароль:")

data = password.encode(encoding="utf-8")
#print("data={}=".format(data))

crypt = hashlib.sha256(data).hexdigest()
print("Crypt={}=".format(crypt))

correct_pass = logindata.get(username, None)
if correct_pass == crypt:
    print("Добро пожаловать")
else:
    print("Доступ запрещён.")

