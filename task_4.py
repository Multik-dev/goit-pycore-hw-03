from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """
    Повертає список користувачів, у яких ДН протягом наступних 7 днів включно (разом із сьогодні).
    Якщо ДН припадає на суботу/неділю — дата привітання переноситься на наступний понеділок.
    
    users: [{"name": str, "birthday": "YYYY.MM.DD"}, ...]
    return: [{"name": str, "congratulation_date": "YYYY.MM.DD"}, ...]
    """
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        try:
            bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except (KeyError, TypeError, ValueError):
            continue  # пропускаємо некоректні записи

        # день народження в поточному році
        bday_this_year = bday.replace(year=today.year)

        # якщо вже минув — беремо наступний рік
        if bday_this_year < today:
            bday_this_year = bday_this_year.replace(year=today.year + 1)

        # перевіряємо вікно [сьогодні; сьогодні+7]
        if today <= bday_this_year <= end_date:
            congr_date = bday_this_year

            # перенос з вихідних на понеділок
            if congr_date.weekday() == 5:      # Saturday
                congr_date += timedelta(days=2)
            elif congr_date.weekday() == 6:    # Sunday
                congr_date += timedelta(days=1)

            result.append({
                "name": user.get("name", ""),
                "congratulation_date": congr_date.strftime("%Y.%m.%d")
            })

    return result


# Приклад
if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Bad Data", "birthday": "1990-01-27"},  # буде пропущено
    ]
    print(get_upcoming_birthdays(users))