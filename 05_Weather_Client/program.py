import collections
import requests

Location = collections.namedtuple('Location', 'city state country')

def main():
    print_header()

    # get the location from the user
    locationText = input('Where do you want the weather report (e.g. Portland, US)? ')
    print(f"You selected {locationText}")

    # convert plaintext over to data we can use
    loc = convertPlaintextLocation(locationText)

    # get report from the API
    key = '6215b88044902e8f262cd476407e0a26'
    data = callWeatherAPI(loc, key)
    print(data)
    

def callWeatherAPI(location, APIkey):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location.city},{location.country}&units=imperial&appid={APIkey}'
    if location.state == '':
        url = url = f'https://api.openweathermap.org/data/2.5/weather?q={location.city},{location.state},{location.country}&units=imperial&appid={APIkey}'
    resp = requests.get(url)
    if resp.status_code in {400, 404, 500}:
        print(f"Error: {resp.text}.")
        return None
    data = resp.json()

    return data

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


