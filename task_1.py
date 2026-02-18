from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Повертає кількість днів між заданою датою та поточною датою.
    
    Параметри:
        date (str): дата у форматі 'YYYY-MM-DD'
    
    Повертає:
        int: кількість днів (може бути від’ємною, якщо дата в майбутньому)
    
    Піднімає:
        ValueError: якщо формат дати некоректний
    """
    try:
        # Перетворюємо рядок у datetime та беремо тільки дату
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Поточна дата без часу
        today = datetime.today().date()
        
        # Різниця між датами
        delta = today - input_date
        
        return delta.days
    
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовувати 'YYYY-MM-DD'.")


# Приклад використання
if __name__ == "__main__":
    print(get_days_from_today("2020-10-09"))