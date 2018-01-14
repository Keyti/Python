#Gra Rock/Paper/Scissors - Kamień/Papier/Nożyce.
#Używamy modułu random.
#Ustalamy najpierw ile rund użytkownik ma grać z komputerem. Po każdej rundzie komputer informuje kto wygrał.
# Po wszystkich rundach również ma się pojawić informacja, kto wygrał i użytkownik miał wygranych,
# ile przegranych a ile remisów.
#Na koniec komputer może zapytać, czy użytkownik chce zagrać jeszcze raz.

import random

rps = ["Rock", "Paper", "Scissors"]

def RockPaperScissors():
    print("Paper beats Rock")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    ile = int(input("How many times do you want to play?  "))
    times = 0
    user_win = 0
    user_draw = 0
    pc_win = 0
    while times != ile:
        choice = input("Rock, Paper or Scissors?  ")
        komp_choice = random.choice(rps)
        if choice == komp_choice:
            print("You choose", choice, "PC choose ", komp_choice)
            user_draw += 1
            times +=1
        else:
            if choice == "Rock" and komp_choice == "Paper":
                print("You choose", choice, "PC choose ", komp_choice)
                pc_win += 1
                times += 1
            elif choice == "Rock" and komp_choice == "Scissors":
                print("You choose", choice, "PC choose ", komp_choice)
                user_win += 1
                times += 1
            elif choice == "Paper" and komp_choice == "Rock":
                print("You choose", choice, "PC choose ", komp_choice)
                user_win == 1
                times += 1
            elif choice == "Paper" and komp_choice == "Scissors":
                print("You choose", choice, "PC choose ", komp_choice)
                pc_win += 1
                times += 1
            elif choice == "Scissors" and komp_choice == "Paper":
                print("You choose", choice, "PC choose ", komp_choice)
                user_win += 1
                times += 1
            else:
                print("You choose", choice, "PC choose ", komp_choice)
                pc_win += 1
                times += 1

    print("You win ", user_win)
    print("You were defeat ", pc_win)
    print("You draw ", user_draw)
    if pc_win > user_win:
        print("You lose whole game :(")
    else:
        print("You win whole game!!")

RockPaperScissors()
wanna = input("Do you want play again? y/n  ")
if wanna == 'y' or wanna == "y":
    RockPaperScissors()
elif wanna == 'n' or wanna == "N":
    print("Thanks for playing ;)")
else:
    print("You little yoker ;) Bye!")
