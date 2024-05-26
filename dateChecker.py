def check_date(month, day, year):
    # check to make sure year is in range of billboard
    if year < 1900 or year > 2024:
        return False, "ERR: INVALID YEAR, VALID YEARS 1900-2024"
    
    # check to make sure month is in range
    if month < 1 or month > 12:
        return False, "ERR: INVALID MONTH, VALID MONTHS 1-12"
    
    # check to make sure day is in range
    if day < 1 or day > 31:
        return False, "ERR: INVALID DAY, VALID DAYS 1-31"
    
    # find whether or not year is leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap = True
    else:
        is_leap = False
    
    # did user enter a leap year date
    if not is_leap and month == 2 and day >= 29:
        return False, "ERR: NONE LEAP YEAR, VALID FEBRUARY DAYS 1-28"
    
    return True, f"DATE ENTERED: {month}/{day}/{year}"