import random
import os

kobiety = ["Ala", "Ela", "Joasia", "Genowefa"]
kobietyNazwiska = ["Jagoda", "Kowalska", "Nowak", "Hesz"]
mezczyzni = ["Janek", "Marek", "Karol", "Filip"]
mezczyzniNazwiska = ["Hucz", "Jurkowski", "Pupiec", "Oleander"]


def imienieinazwisko(plec):
    if plec == "w":
        imie = random.choice(kobiety) + " " + random.choice(kobietyNazwiska)
        print("Generated name is: " + imie)
    elif plec == "m":
        imie = random.choice(mezczyzni) + " " + random.choice(mezczyzniNazwiska)
        print("Generated name is: " + imie)
    else:
      print("Wrong letter :( Only 'w' or 'm' ")



gender = input("What gender should be the name we will generate? Choose w for woman and m for men\n")
imienieinazwisko(gender)
czy = input("Generate again? Choose y for yes or type anything else for exit ;) \n")

while czy == "y":
    os.system('cls')
    gender = input("What gender should be the name we will generate? Choose w for woman and m for men\n")
    imienieinazwisko(gender)
    czy = input("Generate again? Choose y for yes or type anything else for exit \n")
print("Ok. Bye ;)")
