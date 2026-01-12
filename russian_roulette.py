# from random import random
import random   

# russian roulette
print("WELCOME TO THE GAME \n")

print("PRAY THAT YOU SURVIVE")

print("Press ENTER fire the gun")

# print(rightNumber , guessNumber)
def play():
    rounds = 0
    alive = True
    # global rounds
    # global alive
    rightNumber = random.randint(1 ,6)
    guessNumber = random.randint(1 , 6)

    while alive:

        
        input("press enter to fire")
        

        if guessNumber == rightNumber:
            print("you are dead !💀")
            alive = False

            print(f"YOU SURVIVED : {rounds} TIMES ! ")

            print("Want to play again ( YES or NO ) ")

            answer = input("Enter Y or N : ").lower()

            if answer == "y":
                alive = True
                rounds = 0
                rightNumber = random.randint(1 ,6)
                guessNumber = random.randint(1 , 6)
            else:
                print("BYE !")  
                
        else:
            print("you survived this round !👿")
            rounds +=  1
            guessNumber += 1
            if guessNumber > 6:
                guessNumber = 1


play()
