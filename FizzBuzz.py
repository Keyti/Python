#To już szóste zadanie: Fizz / Buzz to zabawa sprawdzająca, czy dzieci potrafią dzielić przez 3 i 5.
# Uczestnicy zabawy liczą po kolei od 1 do (np) 100.#Słowem Fizz zastępują każdą kolejną liczbę podzielną
# przez 3, a słowem Buzz każdą kolejną liczbę podzielną przez 5.

def FizzBuzz():

    start = int(input("Give me the start number:  "))
    stop = int(input("And the finish one:  "))
    lista = []

    for i in range(start, stop + 1, 1):
        lista.append(i)
    print(lista)

    if stop <= start:
        print("Wrong! Stop number is greater then start one! Try again!")
        FizzBuzz()
    else:
        for n in lista:
            if n % 3 == 0 and (n % 5 != 0):
                print(n," Fizz")
            elif n % 5 == 0 and (n % 3 != 0):
                print(n," Buzz")
            elif (n % 5 == 0) and (n % 3 == 0):
                print(n," FizzBuzz")
            else:
                print(n)


print("It's the FizzBuzz game! We will change all numbers divided by 5 with Buzz and all divided by 3 with Fizz")
FizzBuzz()
