def leap_year(year):
    if year % 4:
        return False
    if not year % 400:
        return True
    if not year % 100:
        return False
    return True


def next_date(year, month, day, weekday):
    # Easier to operate with 0 based values: reduce by 1.
    month -= 1
    day -= 1
    weekday -= 1

    month_days = {
        0: 31,
        1: 28,
        2: 31,
        3: 30,
        4: 31,
        5: 30,
        6: 31,
        7: 31,
        8: 30,
        9: 31,
        10: 30,
        11: 31
    }

    if leap_year(year):
        month_days[1] = 29

    current_year = year
    while True:
        weekday, day, month, year = (
            (weekday + 1) % 7,
            (day + 1) % month_days[month],
            (month + (day + 1) // month_days[month]) % 12,
            year + (month // 11) * ((day + 1) // 31))
        yield year, month + 1, day + 1, weekday + 1
        if year > current_year:
            current_year = year
            month_days[1] = 28
            if leap_year(year):
                month_days[1] = 29


def main():
    sundays_on_1st = 0
    for year, month, day, weekday in next_date(1900, 1, 1, 1):
        if year < 1901:
            continue
        if year == 2001:
            break
        if (day == 1) and (weekday == 7):
            print("{}-{:02d}-{:02d}".format(year, month, day))
            sundays_on_1st += 1
    print(sundays_on_1st)


if __name__ == "__main__":
    main()
