import random
rand_num=random.randint(1,3)
if rand_num==1:
    com_side="rock"
elif rand_num==2:
    com_side="paper"
else:
    com_side="scissors"

i=0
while i<5:
    print("You can input 'stop' at anytime to stop the game but nothing else is allowed.")
    user_side=input("Please input your choice (R P S stands for rock paper scissors respectively):")
    if user_side=="R" or user_side=="P" or user_side=="S":
        if user_side=="R":
            if rand_num==1:
                print(" Game is a tie. Try again. 5 more chances")
            elif rand_num==2:
                print("Computer win. You lose. ")
                i+=1
                print(5-i," chances left.")
            else:
                print("You win. You can continue playing.")
        elif user_side=="P":
            if rand_num==2:
                print(" Game is a tie. Try again. 5 more chances")
            elif rand_num==1:
                print("You win. You can continue playing.")
            else:
                print("Computer win. You lose. ")
                i += 1
                print(5 - i, " chances left.")
        else:
            if rand_num==1:
                print("Computer win. You lose. ")
                i += 1
                print(5 - i, " chances left.")

            elif rand_num==2:
                print("You win. You can continue playing.")
            else:
                print(" Game is a tie. Try again. 5 more chances")

    elif user_side=="stop":
        break
    else:
        print("You can only input R, S or P!! ")
        print("Try again. You only have 5 chances totally. ")
        i+=1
        print(5-i," chances left")

print("Game over. Thank you for playing my game.")
