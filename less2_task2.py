def is_year_leap(year):
    if year % 4 == 0:
        return True
    else: return False


year = int(input("Enter a year: "))
result = is_year_leap(year)
print(f"год {year} : {result}")
