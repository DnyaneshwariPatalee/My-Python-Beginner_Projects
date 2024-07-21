import random

item_list = ["Rock" , "Paper" , "Scissor"]

user_choice=input("Enter your choice ==>> Rock , Paper , Scissor =====>>> ")
comp_choice=random.choice(item_list)

print(f"user_choice : {user_choice} , computer_choice : {comp_choice}")

print("<<<<<====================================>>>>>")

if user_choice == comp_choice:
    print("Match Tie!")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper cover Rock , You Win!")
    else:
        print("Scissor cut Paper , Computer Win!")

elif user_choice == "Rock":
    if comp_choice == "Scissor":
        print("Rock break Scissor , You Win!")
    else:
        print("Paper cover Rock , Computer Win!")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cut Paper , You Win!")
    else:
        print("Rock break Scissor , Computer Win!")
