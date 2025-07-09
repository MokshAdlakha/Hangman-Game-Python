import random
from colorama import init, Fore, Style

init(autoreset=True)

def hangman():
    list_words = ['india', 'canada', 'brazil', 'germany', 'france', 'australia',
        'japan', 'china', 'mexico', 'italy', 'spain', 'egypt', 'nigeria',
        'russia', 'sweden', 'norway', 'finland', 'denmark', 'thailand',
        'vietnam', 'indonesia', 'argentina', 'chile', 'peru', 'colombia',
        'poland', 'ukraine', 'turkey', 'iran', 'iraq', 'israel', 'nepal',
        'bangladesh', 'pakistan', 'sri lanka', 'new zealand', 'south korea',
        'north korea', 'kenya', 'south africa', 'morocco', 'algeria', 'tunisia',
        'saudi arabia', 'united kingdom', 'united states', 'philippines',
        'netherlands', 'switzerland', 'austria', 'belgium', 'portugal', 'greece']

    word = random.choice(list_words)
    turns = 10
    guessmade = ''
    entries = set('abcdefghijklmnopqrstuvwxyz')

    while len(word) > 0:
        main_word = ''
        for letter in word:
            if letter in guessmade:
                main_word += letter
            else:
                main_word += "_"

        if main_word == word:
            print(Fore.GREEN + main_word)
            print(Fore.GREEN + "You Won", name, "Congratulations!! 🎉")
            break

        print(Fore.CYAN + "Guess the Country:", ' '.join(main_word))
        guess = input().lower()

        if guess in entries:
            if guess in guessmade:
                print(Fore.YELLOW + "You already guessed that letter.")
                continue
            guessmade += guess
        else:
            print(Fore.YELLOW + "Enter a valid character (a-z only).")
            continue

        if guess not in word:
            turns -= 1
            print(Fore.RED + "Wrong guess! " + str(turns) + " turn(s) left.")
            if turns==9:
                print("9 turns left to guess!!")
                print("-----------------------")
            if turns==8:
                print("8 turns left to guess!!")
                print("-----------------------")
                print("           o           ")
                print("-----------------------")
            if turns==7:
                print("7 turns left to guess!!")
                print("-----------------------")
                print("           o           ")
                print("           |           ")
                print("-----------------------")
            if turns==6:
                print("6 turns left to guess!!")
                print("-----------------------")
                print("           o           ")
                print("           |           ")
                print("          /            ")
                print("-----------------------")
            if turns==5:
                print("5 turns left to guess!!")
                print("-----------------------")
                print("           o           ")
                print("           |           ")
                print("          / \           ")
                print("-----------------------")
            if turns==4:
                print("4 turns left to guess!!")
                print("-----------------------")
                print("          \o           ")
                print("           |           ")
                print("          / \           ")
                print("-----------------------")
                
            if turns==3:
                print("3 turns left to guess!!")
                print("-----------------------")
                print("          \o/           ")
                print("           |           ")
                print("          / \           ")
            if turns==2:
                print("2 turns left to guess!!")
                print("-----------------------")
                print("          \o/ |           ")
                print("           |           ")
                print("          / \           ")
                print("-----------------------")
            if turns==1:
                print("1 turn left to guess!! Dangerrrrr!!!")
                print("------------------------------")
                print("          \o/_|           ")
                print("           |           ")
                print("          / \           ")
                print("-----------------------")
            if turns==0:
                print("Turns Finish")
                print("---------------------------")
                print("        |_\o/_|           ")
                print("           |           ")
                print("          / \           ")
                print("                         ")
                print(Fore.MAGENTA + "You Loose!!! An Innocent Died!! 💀")
                print(Fore.MAGENTA + "The correct word was: " + word)
                break
        else:
            print(Fore.GREEN + "Nice guess!")


print("1. Start Game")
print("2. Instructions")
print("3. Exit")
choice = input("Enter your choice: ")
if choice == '1':
    name = input("Enter Your Name = ")
    print("Welcome to the Hangman Game", name ,"!")
    print("Guess the country in less than 10 attempts")
    hangman()
elif choice == '2':
    print("Guess a letter each turn to reveal the country.")
    print("You have 10 chances before the hangman is completed.")
elif choice == '3':
    print("Goodbye!")
    exit()
else:
    print("Invalid option.")

