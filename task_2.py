import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    # Перевірка валідності параметрів
    if (
        min < 1 or
        max > 1000 or
        min > max or
        quantity < 1 or
        quantity > (max - min + 1)
    ):
        return []

    # Генерація унікальних чисел
    numbers = random.sample(range(min, max + 1), quantity)

    # Повертаємо відсортований список
    return sorted(numbers)


# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)