hidden_word = "Apple"   #This is the secret word that the user has to guess
guess = ""      #This will be the users input
guess_count = 0     #counts how many times the user has guessed
guess_limit = 3     #states the amount of guesses they can have
out_of_guesses = False      #when the guess count hits 3 this will turn true

while guess != hidden_word and not(out_of_guesses):     #we use a while loop to allow the user to guess multiple times
    if guess_count < guess_limit:       #this is to make sure that the user has not guessed 3 times
        guess = input("Enter guess: ")      #this is where the user inputs their answer
        guess_count += 1    #this adds to the guess count to show how many times the user has guessed
    else:
        out_of_guesses = True       #if the conditions on line 7 are not met then that means that the user has guessed 3 times

if out_of_guesses:      #i use a if command to see whether the user has guessed correctly or not
    print("You have ran out of guesses, you lose!")
else:
    print("You guessed the secret word correctly, well done! ")