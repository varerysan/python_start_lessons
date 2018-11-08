import hashlib

logindata = {"admin": "123", 
             "johh": "PasS",
             "user": "test"}

username = input("Введите имя пользователя:")
password = input("Введите пароль:")

data = password.encode(encoding="utf-8")
print("data={}=".format(data))

crypt = hashlib.sha256(data).hexdigest()
print("Crypt={}=".format(crypt))

correct_pass = logindata.get(username,None)
if correct_pass == password:
    print("Добро пожаловать")
else:
    print("Доступ запрещён.")


