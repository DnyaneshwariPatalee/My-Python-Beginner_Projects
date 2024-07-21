import random

def hangman():
    item=['python','java','php','html','css']
    word=random.choice(item)
    turn = 10
    guessmade = ''
    entetries = set('abcdefghijklmnopqrstuvwsyz')

    while len(word)>0:
        main_word = ""

        for letter in word:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + "_"
        
        if main_word == word:
            print(main_word)
            print("You Won!")
            break

        print("Enter your guess",main_word)
        guess = input()

        if guess in entetries:
            guessmade = guessmade + guess
        else:
            print("Enter a valid letter ")
            guess = input()

        if guess not in word:
            turn = turn - 1

            if turn == 9:
                print("9 Turn Left")
                print("===============")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("===============")
            
            if turn == 8:
                print("8 Turn Left")
                print("===============")
                print("|      |       ")
                print("|      |       ")
                print("|")
                print("|")
                print("|")
                print("|")
                print("|")
                print("===============")

            if turn == 7:
                print("7 Turn Left")
                print("===============")
                print("|      |       ")
                print("|      |       ")
                print("|      O       ")
                print("|")
                print("|")
                print("|")
                print("|")
                print("===============")
            
            if turn == 6:
                print("6 Turn Left")
                print("===============")
                print("|      |       ")
                print("|      |       ")
                print("|     _O_      ")
                print("|     | |      ")
                print("|")
                print("|")
                print("|")
                print("===============")
            
            if turn == 5:
                print("5 Turn Left")
                print("===============")
                print("|      |       ")
                print("|      |       ")
                print("|     _O_      ")
                print("|    /| |\     ")
                print("|              ")
                print("===============")

            if turn == 4:
                print("4 Turn Left")
                print("===============")
                print("|      |       ")
                print("|      |       ")
                print("|     _O_      ")
                print("|   \/| |\/    ")
                print("|              ")
                print("===============")

            if turn == 3:
                print("3 Turn Left")
                print("===============")
                print("|      |       ")
                print("|      |       ")
                print("|     _O_      ")
                print("|   \/| |\/    ")
                print("|     | |      ")
                print("===============")

            if turn == 2:
                print("2 Turn Left")
                print("===============")
                print("|      |       ")
                print("|      |       ")
                print("|     _O_      ")
                print("|   \/| |\/    ")
                print("|     |_|      ")
                print("|    /   \        ")
                print("===============")

            if turn == 1:
                print("1 Turn Left")
                print("===============")
                print("|      |       ")
                print("|      |       ")
                print("|     _O_      ")
                print("|   \/| |\/    ")
                print("|     |_|      ")
                print("|   _/   \_    ")
                print("===============")


            if turn == 0:
                print("0 Turn Left")
                print("===============")
                print("===============")
                print("|      |       ")
                print("|      |       ")
                print("|     _O_      ")
                print("|    /| |\     ")
                print("|   / |_| \    ")
                print("|   _/   \_    ")
                print("====      =====")
                print("You Loose!!!")
                print("You let the die a good person!")
                break

name = input("Enter Your Name :")
print(f"Welcome , {name} !")
print("==You Have Only 10 Attempts==")
hangman()