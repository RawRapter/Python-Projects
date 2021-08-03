"""
This Project is Hangman Game.
"""
import random
def hangman():
    word = random.choice(["india" , "batman" , "tiger" , "superman" , "thor" ,
    "pokemon" , "avengers" , "flash" , "earth" , "goku","naruto","people","history","way",
    "art","world","information","map","two","family","government","health","system",
    "computer","meat","year","thanks","music","person","reading","method","data","food","understanding",
    "theory","law","bird","literature","problem","software","control","knowledge","power","ability",
    "economics","love","internet","television","science","library","nature","fact","product","idea",
    "temperature","investment","area","society","activity" ])

    characters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""

        #Creating Guess
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        
        #Win End
        if main == word:
            print("You Got It Correct -> ",main)
            print("You win!")
            break

        #Starting the Guess
        print("Guess the word:" , main)
        guess = input()

        #Checking For Valid Characters
        if guess in characters:
            if guess in guessmade:
                if guess in word:
                    print("Hint: Already Guessed, try another one..")
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
        
        #Hangman Graphic Part as per counter
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("Oops that's wrong, ",turns," Turns Left")
                print("  --------  ")
                print("  |         ")
                print("  |         ")
                print("  |         ")
            if turns == 8:
                print("Oops that's wrong, ",turns," Turns Left")
                print("  ---------  ")
                print("  |          ")
                print("  |   O      ")
                print("  |          ")
                print("  |          ")
            if turns == 7:
                print("Oops that's wrong, ",turns," Turns Left")
                print("  ---------  ")
                print("  |          ")
                print("  |   O      ")
                print("  |   |      ")
                print("  |          ")
            if turns == 6:
                print("Oops that's wrong, ",turns," Turns Left")
                print("  ---------  ")
                print("  |          ")
                print("  |   O      ")
                print("  |   |      ")
                print("  |  /       ")
            if turns == 5:
                print("Oops that's wrong, ",turns," Turns Left")
                print("  ---------  ")
                print("  |          ")
                print("  |   O      ")
                print("  |   |      ")
                print("  |  / \     ")
            if turns == 4:
                print("Oops that's wrong, ",turns," Turns Left")
                print("  ---------  ")
                print("  |          ")
                print("  | \ O      ")
                print("  |   |      ")
                print("  |  / \     ")
            if turns == 3:
                print("Oops that's wrong, ",turns," Turns Left")
                print("  ---------  ")
                print("  |          ")
                print("  | \ O /    ")
                print("  |   |      ")
                print("  |  / \     ")
            if turns == 2:
                print("Oops that's wrong, ",turns," Turns Left")
                print("  ---------  ")
                print("  |  |       ")
                print("  | \ O /    ")
                print("  |   |      ")
                print("  |  / \     ")
            if turns == 1:
                print("Oops that's wrong, ",turns," Turns Left")
                print("Last breaths counting, Take care!")
                print("  ---------  ")
                print("  |  |       ")
                print("  | \|O_/    ")
                print("  |   |      ")
                print("  |  / \     ")
            if turns == 0:
                print("You Loose, Word was: ",word)
                print("You Let a kind Man Die")
                print("  ---------  ")
                print("  |  |       ")
                print("  |  |O      ")
                print("  |  /|\      ")
                print("  |  / \     ")
                break

#Main Part Interface
name = input("Enter your name: ")
print("Welcome" , name,"!!" )
print("Let's The Game Start".center(70,"-"))
print("Try to Guess the Word in less than 10 Attempts")
hangman()