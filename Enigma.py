#Zadanie na dziś: Encrypt / Decrypt Algorithm, czyli algorytm szyfrujący / rozszyfrowujący.
#Zaszyfruj krótką wiadomość.
#Możesz użyć funkcji maketranse() i translate() do operowania na stringach.

def enigma():
    letters = "akotendyjmwrn*^%${"
    charact = "{$%^*nrwmjydnetoka"

    enc = "".maketrans(letters,charact)
    dec = "".maketrans(charact,letters)

    while True:
        ans=input("What do yo want to do? (E)ncrypt, (D)ecrypt or (Q)uit\n")
        if ans == "e" or ans == "E":
            secret = input("Write you message to encrypt\n")
            print("This is encoded message:\n", secret.translate(enc))
        elif ans == "d" or ans == "D":
            secret = input("Write you message to decode\n")
            print("This is encoded message:\n", secret.translate(dec))
        elif ans == "q" or ans == "Q":
            break
        else:
            print("Wrong input!")

enigma()
