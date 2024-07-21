import random
Easy=random.randint(0,9)
Hard=random.randint(10,100)

print('can you guess the no ?')

level = input("Easy Or Hard ? : ")

while(True):
    if level == 'Easy' :
        yournum = int(input("Enter no between 0-9 only :"))
        if Easy == yournum:
            print("You'r Right!")
            break
        elif Easy > yournum:
            print("Your no is too Low! , Try Again ",end="\n")
        else:
            print("Your no is too High! , Try Again ",end="\n")
    else:
        yournum=int(input("Enter the no between 10-100 only :"))
        if Hard == yournum:
            print("You'r Right!")
            break
        elif Hard > yournum:
            print("Your no is too Low! , Try Again ",end="\n")
        else:
            print("Your no is too High! , Try Again ",end="\n")
    