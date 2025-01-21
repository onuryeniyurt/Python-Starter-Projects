import random


word_list=["crocodile","monkey","fly","giraffe","rabbit","goat","elephant"]
word = random.choice(word_list)


# guess=input("Guess a letter:").lower()

# for i in word:
#     if i==guess:
#         print("Right")
#     else:
#         print("Wrong")

#print(word)


placeholder=""
word_length=len(word)
for position in range(word_length):
    placeholder+="_"

    lives=6
game_over=False

correct_letters=[]
wrong_letters=[]

print(placeholder)

while(not game_over): 
    

    guess=input("Guess a letter:").lower()
    display=""
    
    if guess in correct_letters:
        print("You've already guessed this letter")
    
    for i in word:
        if guess==i:
            display+=guess
            correct_letters+=guess
            
        elif i in correct_letters:
            display+=i
            
        else:
            display+="_"
    
            
        
    print(display)
    if guess in wrong_letters:
        print("You've already guessed this letter. It's not in the word. Please try different one")
        
    if guess not in word and guess not in wrong_letters:
        wrong_letters+=guess
        lives-=1
        if lives==0:
            game_over=True
            print("You lose...")

    if "_" not in display:
        print("You win")
        game_over=True
        
