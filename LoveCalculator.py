#Dzisiaj piszemy skrypt do kalkulatora miłości.
#Prosimy użytkownika o wpisanie dwóch imion, a następnie je porównujemy. Możemy przyjąć, że jeśli:
#1. oba imiona zaczynają się na taką samą literę to daje to 20pkt.
#2. oba imiona zaczynają się samogłoską to daje to 10pkt.
#3. oba imiona zaczynają się spółgłoską to daje to 5pkt.
#4. w obu imionach jest taka sama liczba samogłosek to daje to 12 pkt.
#5. w obu imionach jest taka sama liczba spółgłosek to daje to 12 pkt.
#6. w obu imionach jest albo "l" albo "o" albo "v" albo "e" to daje to 7pkt.
#Oczywiście możemy dodać więcej warunków.
#Obliczamy procentową zgodność. Można dodać jakiś ładny tekst na temat związku.

vowel = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "ó", "Ó", "ą", "Ą", "ę", "Ę", "y", "Y"]
consonants = ["b", "B", "c", "C", "ć", "Ć", "d", "D", "f", "F", "g", "G", "h", "H", "j", "J", "k", "K", "l",
              "L", "ł", "Ł", "m", "M","n", "N", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "w", "W",
              "v", "V", "x", "X", "z","Z", "ź", "Ź", "ż", "Ż"]


def tyleSamo(imi,tab):
    same = 0
    for i in range(len(imi)):
        if imi[i] in tab:
            same +=1
        else:
            same = 0
    return same

def love(imienie):
    d = 0
    for a in range(len(imienie)):
        if imienie[a] == "l" or imienie[a] == "L" or imienie[a] == "o" or imienie[a] == "O" or imienie[a] == "v" or imienie[a] == "V" or imienie[a] == "e" or imienie[a] == "E":
            d +=1
    return d

def czychcesz(yn):
    if yn == "y" or yn == "Y":
        zwiazek()
    elif yn == "n" or yn == "N":
        print("Bye ;)")
    else:
        yn == input("Wrong! Only y or n  \n")
        czychcesz(yn)

def zwiazek():
    imieK = input("Type female name:  ")
    imieM = input("Type male name:  ")

    score = 0;
    if imieK[0] == imieM[0]:
        score += 20
    if (imieK[0] in vowel) and (imieM in vowel):
        score += 10
    if (imieK[0] in consonants) and (imieM in consonants):
        score += 5
    if len(imieK) == len(imieM):
        score += 55
    if tyleSamo(imieK,vowel) == tyleSamo(imieM,vowel):
        score += 12
    if tyleSamo(imieK,consonants) == tyleSamo(imieM,consonants):
        score += 12
    if love(imieM) == love(imieK):
        score +=1
    if len(imieK) < len(imieM):
        score += 5

    print("Your love score is ", score)
    print("Lovely!")
    czy = input("Would you like to calculate again? y/n   \n")
    czychcesz(czy)


zwiazek()


