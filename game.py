# import the random module and rename it as "Random_Object"
import random as Random_Object

# initialize variables to keep track of game stats
left_guesses = 5
game_won_count = 0
game_played_count = 0
did_user_win= False
playGame = True
random_num = None

# loop to keep playing the game until the user decides to quit
while(playGame):
    
    # ask the user to guess a number
    userGuess = int(input("Guess a number ("+ str(left_guesses) +" guesses left): "))
    
    # generate a random number between 1 and 100
    random_num = Random_Object.randint(1,100)
    
    # loop to allow the user to keep guessing until they run out of guesses or win
    while(left_guesses != 0):
        left_guesses -= 1
        if(userGuess > random_num):
            print("Too big")
        elif (userGuess < random_num):
            print("Too small")
        else:
            game_won_count += 1
            did_user_win = True
            break
        
        # determine whether to use "guess" or "guesses" in the prompt based on the number of guesses left
        guess_es = " guesses" if left_guesses > 1 else " guess"
        
        # ask the user to guess again
        if(left_guesses == 0):
            break
        else:
            userGuess = int(input("Guess a number ("+ str(left_guesses) + guess_es +" left): "))
        
    # increment the number of games played
    game_played_count += 1
        
    # print a message indicating whether the user won or lost and their stats
    if(did_user_win):
        print("You won! Games won: " + str(game_won_count) + "/"+ str(game_played_count))
    else:
        print("Sorry, you lost. Games won: " + str(game_won_count) + "/"+ str(game_played_count))

    # ask the user if they want to play again
    if (input("Play again? ").lower() == "yes"):
        playGame = True
        left_guesses = 5
        did_user_win= False
    else:
        playGame = False
        
# print a message thanking the user for playing
print("Thank you for playing, have a nice day!")
