from utility import clearTerminal

class Car:
    # class variable
    count = 0

    #at a time ony one constructor works
    # default constructor
    """def __init__(self) -> None:
        self.name = 'name'
        self.company = 'company' 
        self.model = 'model'
        self.varient = 'varient'
        self.color = 'color'
        self.weight = 'weight'
        self.power = 'power'
        self.type = 'type'"""
                
    # parameterized constructor
    def __init__(self, name, company, model, varient, color, weight, power, type) -> None:
        self.name = name
        self.company = company 
        self.model = model
        self.varient = varient
        self.color = color
        self.weight = weight
        self.power = power
        self.type = type
        Car.count += 1

    # instance method 1
    def copy(self):
        return Car(self.name, self.company, self.model, self.varient, self.color, self.weight, self.power, self.type)
    
    # instance method 2
    def showDetails(self):
        print(f"This is a {self.company} brand {self.color} color car named {self.name}. It's model is {self.model}" 
        + f" and {self.varient} varient. It's a {self.power} {self.type} transmission car with {self.weight} weight.")

    @classmethod
    def showTotalNumberOfCars(cls):
        print("Total number of cars are: ", Car.count)

    @staticmethod
    def staticMessage():
        print("You are working with CAR class. Total cars count:", Car.count)


class Addition:
    def __init__(self, firstNum = 0, secondNum = 0) -> None:
        self.firstNum = firstNum
        self.secondNum = secondNum

    def setNumbers(self):
        self.firstNum = int(input("Enter first number: "))
        self.secondNum = int(input("Enter second number: "))

    def showAnswer(self):
        print("Addition of", self.firstNum, "+", self.secondNum, "=", self.firstNum + self.secondNum)

def main():
    myCar = Car('Civic', 'Honda', '2022', 'Turbo 1.6', 'Black', '1250 Kg', '1600 cc', 'Manual')
    myCar2 = myCar.copy()
    myCar.name = 'Civic X'
    print("Object of type ", type(myCar).__name__, "is ", myCar)
    myCar.showDetails()
    myCar2.showDetails()
    Car.showTotalNumberOfCars()
    Car.staticMessage()
    myCar.staticMessage()
    myCar2.staticMessage()
    myCar.showTotalNumberOfCars()
    myCar2.showTotalNumberOfCars()
    sum = Addition()
    sum.setNumbers()
    sum.showAnswer()
    clearTerminal()

main()
