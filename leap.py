def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    # Not divisible by 100
    if year % 4 == 0:
        return True
    return False

    return leap

    year = int((raw_input()))
    print (is_leap(year))
