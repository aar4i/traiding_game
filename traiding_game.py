import random as r 
#create a bag with 10 marbles
bag = ('green','green','green','green','green','white','red','red','black','red',)
#starting amount of money
initial_wallet  = 1000
# current money amount
game_purse = initial_wallet
#result of last round
result = 0
#how many rounds
rounds = int(input('How many rounds: '))
#last marble
#last_marble = 
# welcome user to game
print(f'Welcome to the game. You have {initial_wallet}$. Good luck!')
# loop drawing marbles
for round in range(1, rounds+1):
    #how much was bet
    bet = int(input(f'Make your bet. You got {game_purse}$ in your wallet. \nYour current round: {round}. \nHow much is your bet? '))
    #draw marble
    drawn_marble = r.choice(bag)
    # win or loss
    if drawn_marble == 'green':
        result = bet
    elif drawn_marble == 'black':
        result = bet * 10
        print("You have drawn a black marble. 😊")
    elif drawn_marble == 'white':
        result = bet * -5
        print("You have drawn a white marble. 😥")
    else :
        result = -bet    
    #calc win or loss/ result and new amount/purse
    game_purse += result
    #lose game if lose half of money
    if game_purse <= initial_wallet*0.5:
        print(f'You lost! Your result was: {result}$. Your amount is now: {game_purse}$.')
        break
    #print results
    print(f'You got: {game_purse}$. In last round you got: {result}$.')
# print final results
print(f'You start with {initial_wallet}$, now you have {game_purse}$. \nYour gain: {(game_purse - initial_wallet)/initial_wallet * 100}%.')
