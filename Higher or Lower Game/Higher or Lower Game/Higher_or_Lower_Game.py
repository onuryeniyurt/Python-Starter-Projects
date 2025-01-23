import random
from game_data import data

def generate_random():
    rnd=random.randint(0,len(data))
    print(data[rnd]['name'], data[rnd]['description'] + " from " + data[rnd]['country'])
    return int(data[rnd]['follower_count'])
    
def compare():
    game_lose=False
    score=0
    while not game_lose:
        print("Compare A:")
        A=generate_random()
        print("VS")
        print("Against B:")
        B=generate_random()
        
        ans=input("Which one has the most follower?").lower()
   
        if ans=='a' and A>=B:
            score+=1
            print(f"You are right! Your current score is: {score}")
        elif ans=='b' and B>=A:
            score+=1
            print(f"You are right! Your current score is: {score}")
        else:
            print(f"Sorry, you lose :( Your final score is: {score}")
            game_lose=True
        print("\n"*2)


game_on=True  
while game_on:    
    compare()
    _ans=input("Do you want to play again? (Y/N)").lower()
    if _ans=='n':
        game_on=False
        
    print("\n"*20)
