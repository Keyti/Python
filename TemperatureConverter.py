#Zadanie 4 - Temperature Converter
#Tworzymy program, który przelicza z Fahrenheitów na Celsiusze lub odwrotnie.
#Dodatkowo można jeszcze zadanie rozwinąć:
#Komputer powinien podać nam następujące informacje:
#1. jeśli temperatura C jest poniżej -273.15, że liczba jest niewłaściwa, ponieważ ta temperatura jest poniżej zera absolutnego
#2. jeśli temperatura C wynosi między - 273.15 a 0 stopni, że temp. jest poniżej zera
#3. jeśli temperatura C wynosi 0, to jest to temperatura zamarzania
#4. jeśli temperatura wynosi 100 C, to jest to temperatura wrzenia.

#Można zrobić też opcję dotyczącą pogody - bardzo mroźno, przymrozek, chłodno, ciepło, gorąco, itd.
#To oczywiście są tylko moje propozycje.

def temperatury(unit):
    if unit == 'c' or unit == 'C':
        temp = int(input("Write the temperature:\n"))
        fare=32+(9/5*temp)
        print("This is %d in Fahrenheit" % fare)
    elif unit == 'f' or unit == 'F':
        temp = int(input("Write the temperature:\n"))
        celc=5/9*(temp-32)
        if celc < -273.15:
            print("The number is incorrect because this temperature is below absolute zero. There can't be %d Celsius!" % celc)
        elif -273.15 < celc < 0:
            print("Temperature is below 0. Exactly: %d Celsius" % celc)
        elif celc == 0:
            print("This is the freezing temperature! The %d Celsius" % celc)
        elif celc == 100:
            print("This is the boiling temperature! The %d Celsius" % celc)
        else:
            print("This is %d Celsius" % celc)
    else:
        unitery2=input("Wrong unit. Try again. Pick the unit: 'C'elsius or 'F'arenheit\n")
        temperatury(unitery2)
        
unitery=input("Pick the unit: 'C'elsius or 'F'arenheit\n")
temperatury(unitery)
