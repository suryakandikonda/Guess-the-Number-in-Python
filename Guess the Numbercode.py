# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math
range = 100
secret_number = 0
guesses = 0


# helper function to start and restart the game
def new_game():
    global range
    global guesses
    global secret_number
    secret_number = random.randrange(0,range)
    
    if range == 100:
        guesses = 7
    elif range == 1000:
        guesses = 10
    print "Developed by : SURYA KANDIKONDA"
    print "New Game, Range is from 0 to ", range
    print "No. of remaining guesses are " ,guesses
    

# define event handlers for control panel
def range100():
    global range
    range = 100
    new_game()

    

def range1000():
    global range
    range = 1000
    new_game()
    
def input_guess(guess):
    guess = int(guess)
    global secret_number
    global guesses
    print ""
    print "Guess was " , guess
    if guess < secret_number and guesses !=1:
        guesses = guesses - 1 
        print "No. of remaining guesses are ",guesses
        print "Lower!"
    elif guess > secret_number and guesses != 1:
        guesses = guesses - 1
        print "No. of remaining guesses are ",guesses
        print "Higher!"
    elif guess == secret_number and guesses != 1:
        guesses = guesses - 1 
        print "No. of remaining guesses are ",guesses
        print "Correct!"
        print ""
        new_game()
    else :
        print "Secret_number is " , secret_number
        print ""
        print "Sorry!. The guesses are completed. New game started" 
        new_game()
    
   

    
# create frame
frame = simplegui.create_frame("Guess the Number" , 300,300)
frame.add_button("Range is [0,100)", range100 , 200)
frame.add_button("Range is [0,1000)", range1000 , 200)
frame.add_input("Enter your Guess", input_guess,100)




# register event handlers for control elements and start frame


# call new_game 
new_game()
frame.start()

