import random

kobiety = ["Ala", "Ela", "Joasia", "Genowefa"]
kobietyNazwiska = ["Jagoda", "Kowalska", "Nowak", "Hesz"]
mezczyzni = ["Janek", "Marek", "Karol", "Filip"]
mezczyzniNazwiska = ["Hucz", "Jurkowski", "Pupiec", "Oleander"]


def imienieinazwisko(plec):
    if plec == "k":
        imie = random.choice(kobiety)
    elif plec == "m":
        imie = random.choice(mezczyzni)
    else:
        plec = input("Wpisz k dla kobiety i m dla mężczyzny")
    if plec == "k":
        nazwisko = random.choice(kobietyNazwiska)
    elif plec == "m":
        nazwisko = random.choice(mezczyzniNazwiska)
    else:
        plec = input("Wpisz k dla kobiety i m dla mężczyzny")

    print("Wygenerowano imię: " + imie +" " + nazwisko)

gender = input("Jakiej płci ma być wygenerowane imię i nazwisko? Wpisz k dla kobiety i m dla mężczyzny\n")
imienieinazwisko(gender)
czy = input("Czy chcesz generować jeszcze raz? (y)es lub cokolwiek ;) \n")

while czy == "y":
    gender = input("Jakiej płci ma być wygenerowane imię i nazwisko? Wpisz k dla kobiety i m dla mężczyzny\n")
    imienieinazwisko(gender)
    czy = input("Czy chcesz generować jeszcze raz? (y)es lub cokolwiek ;) \n")
print("No to cześć ;)")