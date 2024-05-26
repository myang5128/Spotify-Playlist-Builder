from dateChecker import check_date

def pick_date():
    year = input("What year do you want to travel to: (YYYY format)\n")
    while len(year) != 4 or year.isdigit() == False:
        year = input("What year do you want to travel to: (YYYY format)\n")
    
    month = input("What month do you want to go to: (MM format) \n")
    while len(month) > 2 or month.isdigit() == False:
        month = input("What month do you want to go to: (MM format) \n")
        
    day = input("What day do you want to go to: (DD format) \n")
    while len(day) > 2 or day.isdigit() == False:
        day = input("What day do you want to go to: (DD format) \n")
    
    year = int(year)
    month = int(month)
    day = int(day)
    
    return month, day, year

def date_selection():
    
    month, day, year = pick_date()
    correct, message = check_date(month, day, year)
    print(message)
    while not correct:
        month, day, year = pick_date()
        correct, message = check_date(month, day, year)
        print(message)
    
    
    year, month, day = str(year), str(month).zfill(2), str(day).zfill(2)
    date = f"{year}-{month}-{day}"
    return date