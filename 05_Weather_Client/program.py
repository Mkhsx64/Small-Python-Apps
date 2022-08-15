
def main():
    print_header()
    # get the location from the user
    locationText = input('Where do you want the weather report (e.g. Portland, US)? ')
    print(f"You selected {locationText}")
    
    get_html()
    parse_html()
    display()


def display():
    pass


def parse_html():
    pass


def get_html():
    pass


def print_header():
    pass


if __name__ == '__main__':
    main()


