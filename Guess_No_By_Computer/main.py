import random
import math

def demo2(guess):
    feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? :").lower()
    if feedback in ['h', 'l', 'c'] :
        return feedback
    else:
        print("Please enter 'h', 'l', 'c' ")


def demo1(low , high):
    return random.randint(low , high )
    

def main():
    print("Think of a number between 1 and 100, and I will try to guess it.")
    low = 1
    high = 100
    guess = demo1(low , high)
    feedback = demo2(guess)


    while feedback != 'c':
        if feedback == 'h':
            high = guess -1
        elif feedback =='l':
            low = guess + 1

        
        if low > high:
            print("Hmm, something went wrong. Let's start over.")
            low, high = 1, 100
        
        guess = demo1(low, high)
        feedback = demo2(guess)

    print(f"I guessed it! Your number is {guess}.")


if __name__ == "__main__":
    main()
