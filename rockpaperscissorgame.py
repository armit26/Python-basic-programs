import random

print ("Welcome to Rock Paper Scissor Game")

choices = ["rock", "paper", "scissor"]

user=input("Enter your choice rock, paper or scissor = ").lower()
computer=random.choice(choices)

print ("Computer =", computer)

#Tie case
if user == computer:
    print("It's a Tie")

#User's winning cases
elif user == "rock" and computer == "scissor":
    print("Congratulations! You won!")
elif user == "paper" and  computer == "rock":
    print("Congratulations! You won!")
elif user == "scissor" and computer == "paper":
    print("Congratulations! You won!")

#User's losing cases
elif user == "rock" and computer == "paper":
    print("You Lost, Better luck next time")
elif user == "paper" and computer == "scissor":
    print("You Lost, Better luck next time")
elif user == "scissor" and  computer == "rock":
    print("You Lost, Better luck next time")

else:
    print("Invalid input, Try again")






