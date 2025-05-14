import random

# Генеруємо великий список чисел з випадковими повторами
numbers = [random.randint(1, 1000) for _ in range(10000)]

# Створюємо словник для підрахунку кількості повторів
counts = {}

for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

# Знаходимо число з найбільшою кількістю повторень
max_number = max(counts, key=counts.get)
max_count = counts[max_number]

# Виводимо результат
print(f"Число {max_number} повторюється найбільше разів: {max_count}")
