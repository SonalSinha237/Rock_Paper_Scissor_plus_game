# numbering:-
# rock-0
# spock-1
# paper-2
# lizard-3
# scissor-4
# Ply-Player , Comp-Computer , Ch - Choice , Num - Number

import random

PlyName=str(input('Enter your name:'))

# GAME INSTRUCTIONS 

print('\nHEY',PlyName.upper(),'!!!')
print('''
WELCOME TO THE GAME ROCK - SPOCK - PAPER - LIZARD - SCISSOR !!! \n
Hope you are in the pink of health :)
Let\'s start the game.

Let me take you through the instructions of this game ~

-You can enter any one of the 5 choices (one at a time) ~ Rock, Paper, Scissor, Lizard, Spock.
 These options work as follows:
-> Rock can defeat scissor & lizard but loses against paper & spock
-> Paper can defeat rock & spock but loses against scissor & lizard
-> Scissor can defeat paper & lizard but loses against rock & spock
-> Lizard can defeat spock & paper but loses against rock & scissor
-> Spock can defeat scissor & rock but loses against lizard & paper

You will enter your choice first and then computer will play its turn.
You can play as many rounds as you want.
1 point will be given for winning a round & 0 if you lose or if it\'s a tie.
Final scores along with the winner will be declared at the end.

ALL THE BEST & ENJOY :)''')
print('*****************************************************************************')

# CONVERTING USER'S STRING INPUT TO ITS CORRESPONDING VALUE (HELPER FUNCTION)
    
def name_to_number(ply_ch): 
    value = -1
    if ply_ch == 'rock':
        value = 0
    elif ply_ch == 'spock':
        value = 1
    elif ply_ch == 'paper':
        value = 2
    elif ply_ch == 'lizard':
        value = 3
    elif ply_ch == 'scissor':
        value = 4
    else:
        print('Sorry! but that\'s an invalid input. Select one from rock, paper, scissor, spock, lizard.')
    return value
 
# CONVERTING COMPUTER'S CHOICE (IN NUMBER) TO ITS CORRESPONDING NAME (HELPER FUNCTION)
       
def number_to_name(CompNum):
    if CompNum == 0:
        choice = 'rock'
    elif CompNum == 1:
        choice = 'spock'
    elif CompNum == 2:
        choice = 'paper'
    elif CompNum == 3:
        choice = 'lizard'
    elif CompNum == 4:
        choice = 'scissor'
    return choice

# INITIALISING USER & COMPUTER'S SCORE

player_score=0
computer_score=0

# MAIN GAME FUNCTION

def rpsls():
    global player_choice
    global player_score
    global computer_score
    player_choice = str(input('Enter your choice:'))  # user's choice input
    print('')
    ply_ch = player_choice.lower()  # converting user's input string into lowercase so that all the cases like camel, toggle, upper can be dealt.  
    print('You chose',ply_ch)       # printing user's choice
    
    PlyNum=name_to_number(ply_ch)   
    if PlyNum != -1:
        CompNum=random.randrange(0,5)       # computer's choice within a range (integer) if user enters a valid choice
        comp_ch = number_to_name(CompNum)   # converting computer's choice() to option name
        print('Computer chose',comp_ch)     # printing computer's choice
        Score = (PlyNum - CompNum) % 5      # score calculation of each round
        if Score == 0:
            print('It\'s a tie')
            print('****************************************')
        elif Score == 1 or Score == 2:
            player_score+=1                     # for user's final score
            print('Congrats, you won this round :)')
            print('***********************************************')
        elif Score == 3 or Score == 4:
            computer_score+=1                   # for computer's final score
            print('Oh! Computer won this round')
            print('******************************************')
    
    print('\nWanna play another round?')        # asking user for another round of game
    reply=str(input('Waiting for your reply in yes or no:'))
    #print('****************************************')
    reply=reply.lower()
    if reply == 'yes':
        rpsls()
    elif reply == 'no':
        print('Okay, No problem :)')
    else:
        print('Invalid reply.\nSee the final result')
    
# MAIN FUNCTION CALL        
rpsls()     

# FINAL SCORE & WINNER DECLARATION

print('****************************************')
print('\nComputer\'s score:',computer_score)
print('Your score:',player_score)

if player_score > computer_score:
    print('\nCONGRATULATIONS',PlyName.upper(),'YOU ARE THE WINNER!!!!')
elif computer_score > player_score:
    print('\nCOMPUTER WINS!\nBETTER LUCK NEXT TIME',PlyName.upper(),':)')
elif computer_score == player_score:
    print('\nCONGRATS TO BOTH OF YOU!!! IT\'S A TIE')
    
print('\nBYE, SEE YOU :)')


        




    
    
    
    
    
    
    
    
    
    
    
      
    