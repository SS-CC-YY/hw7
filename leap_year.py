
def leap_year(year):
    if year < 0:
        raise ValueError ("Invalid input")

    
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return "It is a leap year!"
    else:
        return "It is not a leap year!"

def main():
    print(leap_year(2020))

if __name__ == "__main__":
    main()