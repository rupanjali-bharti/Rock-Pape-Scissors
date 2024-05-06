import random
import sys

comp_count =0
user_count = 0

print("select your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    
for i in range(0,5):
      #for i in range(0,3):
    user_choice = int(input("Enter your choice :"))
    print()
    if user_choice  == 1:
        choice = "Rock"
    elif user_choice  == 2:
        choice = "Paper"
    elif user_choice == 3:
        choice = "Scissors"    

    l=["rock", "paper", "scissors"]
    comp_choice = random.choice(l)

    print("Your choice :", choice)
    print("python choice :", comp_choice)

    if user_choice == 1 and comp_choice == "scissors" or user_choice == 2 and comp_choice == "rock" or user_choice == 3 and comp_choice == "paper" :
        user_count += 1
        print("You won")
    elif user_choice == 1 and comp_choice == "paper" or user_choice == 2 and comp_choice == "scissor" or user_choice == 3 and comp_choice == "rock" :  
        comp_count += 1 
        print("Python won")
    elif user_choice == 1 and comp_choice == "rock" or user_choice == 2 and comp_choice == "paper" or user_choice == 3 and comp_choice == "scissors" :  
        print("match was draw")

    print()

print("you won ", user_count, "times , out of 5" )
print("python won ", comp_count, "times")

            

         




        