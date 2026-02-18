import re

def normalize_phone(phone_number: str) -> str:
    # Видаляємо всі символи, крім цифр і +
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())

    # Якщо номер починається з +
    if cleaned.startswith("+"):
        # Залишаємо тільки один + і цифри після нього
        digits = re.sub(r"\D", "", cleaned)
        return "+" + digits

    # Якщо номер починається з 380 — додаємо +
    if cleaned.startswith("380"):
        return "+" + cleaned

    # В інших випадках додаємо код України +38
    digits = re.sub(r"\D", "", cleaned)
    return "+38" + digits


# Приклад використання
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)