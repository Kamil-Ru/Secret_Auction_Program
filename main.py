from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
aution_bid = {}

game_on = True

while game_on:
    
    clear()
    print(logo)
    name = input("What is your name?\n")
    bid = int(input("What's is your bid?\n"))
    aution_bid[name] = bid
    
    ask_for_player = True
    while ask_for_player:
    
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    
        if other_bidders == 'no':
            game_on = False
            ask_for_player = False
            
        elif other_bidders == 'yes':
            ask_for_player = False
                       
winner = ['',0]
for key, value  in aution_bid.items():
    if value > winner[1]:
        winner = [key, value]
        
clear()
print(f'The winner is {winner[0]} with a bid of {winner[1]}')
      
