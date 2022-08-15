while (1):
    year = input("Insert year: ")
    year = int(year)
    if year == 0:
        exit()
    if (year % 400 == 0 or year % 4 == 0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

