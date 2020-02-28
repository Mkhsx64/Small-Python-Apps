import datetime


def print_header():
    print('------------------------------')
    print('        BIRTHDAY APP')
    print('------------------------------')
    print()


def get_birthday_from_user():
    print('When were you born" ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))
    
    bday = datetime.date(year, month, day)
    return bday


def compute_days_between_dates():
    pass


def print_birthday_information():
    pass

def main():
    print_header()
    bday = get_birthday_from_user()
    now = None
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)


main()
