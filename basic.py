from time import sleep
from os import system
from requests import get, codes
from keyboard import read_key
from json import loads
from geopy.geocoders import Nominatim
import geocoder


# Method for option 1
def getUserDetails():
    name = input("What's your name? ")
    age = input("What's your age? ")
    country = input("What's your origin(birth country)? ")
    university = input("Name the university you went to for graduation? ")
    print(f"{name} is {age} years old, born in {country} in year {2023 - int(age)} and studied at {university}.")

# Method for option 2
def getAllCountriesDetails():
    api_url = 'https://restcountries.com/v3.1/all'
    try:
        response = get(api_url)
        if response.status_code == codes.ok:
            printCountriesNames(response.text)
        else:
            print("Error: ", response.status_code, response.text)
    except:
        print(f"Error: Filed to get response from {api_url}.")

# Method for option 3
def checkPrimeNumber():
    number = int(input("Enter a number: "))
    isPrime = True
    if number < 2:
        isPrime = False
    elif number > 4:
        for num in range(2, round(number/3)+1):
            if (number % num == 0):
                isPrime = False
                break
    if isPrime:
        print(number, "is a Prime Number.")
    else:
        print(number, "is not a Prime Number.")

# Method for option 4
def printMyLocation():
    geolocator = Nominatim(user_agent="my_app")
    g = geocoder.ip('me')
    location = f"{g.lat}, {g.lng}"
    address = geolocator.reverse(location)
    print(f"Your location is: {address.address}")

def printCountriesNames(response):
    jsonResponse = loads(response)
    for index, country in enumerate(jsonResponse):
        print(index + 1, country['name']['official'])

def printMethodDetails():
    print("Select a number from options listed below!")
    print("1. Get user details.")
    print("2. Get all countries details.")
    print("3. Check if a number is prime.")
    print("4. Get your current location.")

def selectAndExecuteMethod():
    functionNumber = input("Enter the function number: ")
    if functionNumber == "1":
        getUserDetails()
    if functionNumber == "2":
        getAllCountriesDetails()
    if functionNumber == "3":
        checkPrimeNumber()
    if functionNumber == "4":
        printMyLocation()
    else:
        close(True)
        selectAndExecuteMethod()


def close(instant):
    if not(instant):
        sleep(1)
        print("Thanks for using our services. Press any key to exit.")
    if read_key():
        system('clear')

def main():
    printMethodDetails()
    selectAndExecuteMethod()
    close(False)
    
main()
