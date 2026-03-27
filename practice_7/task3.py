correct = "FIFA"
for attempt in range(1, 4):
    answer = input("Введите название игры:\n>>> ")
    if answer == correct:
        print(f"Поздравляем! Вы угадали с попытки № {attempt}")
        break