
def main():
    print_header()
    # get the location from the user
    locationText = input('Where do you want the weather report (e.g. Portland, US)? ')
    print(f"You selected {locationText}")

    # convert plaintext over to data we can use
    location = convertPlaintextLocation(locationText)
    print(f"Location = {location}")
    
    get_html()
    parse_html()
    display()

def convertPlaintextLocation(plaintText):
    pass

def display():
    pass


def parse_html():
    pass


def get_html():
    pass


def print_header():
    # heading for the application
    print('--------------------------------')
    print('         WEATHER CLIENT         ')
    print('--------------------------------')
    print()


if __name__ == '__main__':
    main()


