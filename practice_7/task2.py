forbidden = "?*^$№@_"
login = input("Введите логин: \n>>> ")
for char in login:
    if char in forbidden:
        print(f"Запрещённый символ: {char}")