import random

cards={'A':11,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'K':10,'Q':10}

admin_1=random.choice(list(cards.keys()))
admin_2=random.choice(list(cards.keys()))

player_1=random.choice(list(cards.keys()))
player_2=random.choice(list(cards.keys()))

admin_total=int(cards[admin_1]) + int(cards[admin_2])
player_total=int(cards[player_1]) + int(cards[player_2])

print(f"Admin's card is {admin_1}")
print(f"Your cards are {player_1} , {player_2}")

_play=True
while (_play):
    ans=input("Do you want to hit a card? (Y/N)").lower()
    
    if(ans=='n'):
        print(f"Admin's cards are {admin_1}, {admin_2}")
        if player_total==21:
            print("YOU WIN!")
        else:
            while admin_total<17:
                new_admin=random.choice(list(cards.keys()))
                print(f"Admin's card: {new_admin}")
                admin_total+=int(cards[new_admin])
            if admin_total>player_total and admin_total<=21:
                print(f"You lose. your cards:{player_total} and admin's cards: {admin_total}")
            elif player_total>admin_total:
                print(f"You win. your cards:{player_total} and admin's cards: {admin_total}")
            elif player_total==admin_total:
                print(f"DRAW. the cards are{admin_total}")
            _play=False
    else:
        player_3=random.choice(list(cards.keys()))
        player_total+=int(cards[player_3])
        print(f"Your card is: {player_3}")
        print(f"Your total cards are: {player_total}")
        if player_total>21:
            print(f"YOU LOSE admin's cards are: {admin_total}")
            _play=False



