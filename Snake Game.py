import random

list = ["s","w","g"]

chances = 10
No_of_computer_point  =  0
No_of_chance = 0
No_of_Human_point = 0

while No_of_chance<chances:
    User_input = input("Snake, Water,Gun:")
    Computer_random = random.choice(list)

    if User_input==Computer_random:
        print("Its tie")

    elif User_input == "s" and Computer_random == "g":

        print(f"your choice{User_input} and computer choice{Computer_random}")
        No_of_computer_point=No_of_computer_point+1
        print("Computer won")

    elif User_input == "s" and Computer_random== "w":
        print(f"your choice{User_input} and computer choice{Computer_random}")
        No_of_Human_point=No_of_Human_point+1
        print("You won")

    elif User_input == "g" and Computer_random == "s":
        print(f"your choice{User_input} and computer choice{Computer_random}")
        No_of_Human_point=No_of_Human_point+1
        print("You won")

    elif User_input == "g" and Computer_random == "w":
        print(f"your choice{User_input} and computer choice{Computer_random}")
        No_of_computer_point=No_of_computer_point+1
        print("Computer won")

    elif User_input == "w" and Computer_random == "s":
        print(f"your choice{User_input} and computer choice{Computer_random}")
        No_of_computer_point=No_of_computer_point+1
        print("Computer won")

    elif User_input == "w" and Computer_random == "g":
        print(f"your choice{User_input} and computer choice{Computer_random}")
        No_of_computer_point=No_of_computer_point+1
        print("Computer won")

    else:
        print("You have entered wrong input\n")

    No_of_chance = No_of_chance + 1
    print(f"{chances-No_of_chance} is left out of {chances}\n")

print("Game over")

if No_of_computer_point > No_of_Human_point:
    print("Computer won the game")

elif  No_of_computer_point < No_of_Human_point:
    print("You won the Game")

else:
    print("Its tie")
    
       

