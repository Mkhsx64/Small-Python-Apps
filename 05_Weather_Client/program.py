import collections

Location = collections.namedtuple('Location', 'city state country')

def main():
    print_header()

    # get the location from the user
    locationText = input('Where do you want the weather report (e.g. Portland, US)? ')
    print(f"You selected {locationText}")

    # convert plaintext over to data we can use
    loc = convertPlaintextLocation(locationText)
    print(loc)

def convertPlaintextLocation(plaintText):
    # if no input return None
    if not plaintText or not plaintText.strip():
        return None
    
    parts = plaintText.lower().split(',')
    parts = [x.strip(' ') for x in parts]

    # Need to set up logic for which value coincides to data we need to pass to the API
    city = ''
    state = ''
    country = 'us'
    if len(parts) == 1:
        city = parts[0]
    elif len(parts) == 2:
        city = parts[0]
        state = parts[1]
    elif len(parts) == 3:
        city = parts[0]
        state = parts[1]
        country = parts[2]
    else:
        return None
    
    return Location(city, state, country)


def print_header():
    # heading for the application
    print('--------------------------------')
    print('         WEATHER CLIENT         ')
    print('--------------------------------')
    print()


if __name__ == '__main__':
    main()


