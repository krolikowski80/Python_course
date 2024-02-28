def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Sprawdza, czy rok jest przestępny
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Pobranie danych wejściowych od użytkownika
year = int(input("Enter a year: ")) # Wprowadź rok
month = int(input("Enter a month: ")) # Wprowadź miesiąc

# Wywołanie funkcji i wyświetlenie wyniku
days = days_in_month(year, month)
print(f"Number of days: {days}")
