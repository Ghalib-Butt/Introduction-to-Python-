from time import sleep
from os import system
from requests import get, codes
from keyboard import read_key
from json import loads

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
        for num in range(2, round(number/3)):
            if (number % num == 0):
                isPrime = True
                break
    if isPrime:
        print(number, "is a Prime Number.")
    else:
        print(number, "is not a Prime Number.")

def printCountriesNames(response):
    jsonResponse = loads(response)
    for index, country in enumerate(jsonResponse):
        print(index + 1, country['name']['official'])

def printMethodDetails():
    print("Select a number from options listed below!")
    print("1. Get user details.")
    print("2. Get all countries details.")
    print("3. Check if a number is prime.")

def selectAndExecuteMethod():
    functionNumber = input("Enter the function number: ")
    if functionNumber == "1":
        getUserDetails()
    if functionNumber == "2":
        getAllCountriesDetails()
    if functionNumber == "3":
        checkPrimeNumber()

def close():
    sleep(1)
    print("Thanks for using our services. Press any key to exit.")
    if read_key():
        system('clear')

def main():
    printMethodDetails()
    selectAndExecuteMethod()
    close()
    
main()
