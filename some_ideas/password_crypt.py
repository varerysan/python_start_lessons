logindata = {"admin": "123", 
             "johh": "PasS",
             "user": "test"}

username = input("Введите имя пользователя:")
password = input("Введите пароль:")

correct_pass = logindata.get(username,None)
if correct_pass == password:
    print("Добро пожаловать")
else:
    print("Доступ запрещён.")
