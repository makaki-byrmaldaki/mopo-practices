while True:
    action = input("Введите 1 – рекомендация, 2 – розыгрыш, off – завершить\n>>> ")
    if action == "1":
        pref = input("Введите предпочтение:\n>>> ")
        if pref == "спорт":
            print("Подкаст Убойный спорт")
        else:
            print("Новый альбом Канье Уэста")
    elif action == "2":
        for attempt in range(1, 4):
            group = input("Введите название группы\n>>> ")
            if group == "Queen":
                print("Вы выиграли билет на концерт!")
                break
    elif action == "off":
        print("Программа завершена")
        break