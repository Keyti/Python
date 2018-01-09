#Higher/Lower - gra, w której użytkownik zgaduje liczbę, a komputer mu podpowiada, czy liczba jest większa od podanej czy mniejsza. Określamy w jakim przedziale ma być ta liczba i ile rund ma toczyć się gra.
#lub:
#Heads/Tails - orzeł czy reszka - komputer oblicza prawdopodobieństwo wypadnięcia orła np. w 100 rzutach i sprawdza, czy jest to zgodne z naszym przewidywaniem(czy zgadliśmy ile razy wypadnie np.orzeł).
#Oczywiście to są tylko sugestie. Pod tym postem wrzucajcie swoje linki, dzielcie się postępami.

# https://repl.it/@Keyti27/HighLow

import random
import  os

def zgadnij(liczba):
    guess = int(input("Guess a number between 1 and 50. You have only 5 chances\n"))
    time = 1
    guessing = 5

    while guess != liczba:
        if time == 5:
            break
        if guess > liczba:
            print("Chances last: ", guessing - time)
            guess = int(input("Guess again. Your number is greater then chosen number\n"))
            time = time + 1
        elif guess < liczba:
            print("Chances last: ", guessing - time)
            guess = int(input("Guess again. Your number is smaller then chosen number\n"))
            time = time + 1
        elif guess == liczba:
            print("You win!")
        else:
            print("You lose! The number was: ", liczba)

    if guess == liczba:
        print("You win!")
    else:
        print("You lose! The number was: ", liczba)

numer = random.randint(1,50)
zgadnij(numer)
czy = input("Wanna play again? y/n\n")

if czy == "y":
    liczba2 = random.randint(1,50)
    zgadnij(liczba2)
else:
    print("OK. Thanks for play :)")
