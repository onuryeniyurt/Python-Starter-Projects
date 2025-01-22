import random

game_over=False

def game():
    num=random.randint(1,101)
    lives=0
    you_win=False
    while not you_win:
        ans=input("I am thinking of a number between 1 and 100. Dou you want to easy or hard mode?:").lower()
    
        if ans=='easy':
            lives=10
            print("You choose easy mode. You have 10 attempts")
        else:
            lives=5
            print("You choose easy mode. You have 5 attempts")
        
        while lives>0 and not you_win:
            guess=int(input("What is your guess?"))
            
            if guess>num:
                print("Too high")
                lives-=1
                print(f"You have {lives} attempts left.")
            elif guess<num:
                print("Too low")
                lives-=1
                print(f"You have {lives} attempts left.")
            else:
                print("You won!")
                you_win=True
            


while not game_over:
    game()
                
