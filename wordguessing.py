import random
word_bank = ['Strawberry', 'Eclipse', 'Chandelier', 'Ketchup', 'Toothpaste', 'Rainbow', 'Boardgame', 'Beehive', 'Lemon', 'Wreath', 'Waffles', 'Bubble', 'Whistle', 'Snowball', 'Bouquet', 'Headphones', 'Fireworks', 'Igloo', 'Ferris wheel', 'Banana peel', 'Lawnmower', 'Summer', 'Whisky', 'Cupcake', 'Sleeping bag', 'Bruise', 'Fog', 'Crust', 'Battery', 'Paris', 'Beach', 'Mountains', 'Hawaii', 'Mount Rushmore', 'USA', 'Hospital', 'Attic', 'Japan', 'Library', 'Desert', 'Mars', 'Washington DC', 'Las Vegas', 'Train station', 'North Pole', 'Farm', 'Disney World', 'Mexico', 'Giraffe', 'Koala', 'Wasp', 'Scorpion', 'Lion', 'Salamander', 'Dolphin', 'Frog', 'Panda', 'Platypus', 'T rex', 'Meerkat', 'Eagle', 'Mailman', 'Superman', 'Justin Beiber', 'Cowboy', 'Alexander Hamilton', 'Robin Hood', 'Vampire', 'Pirate', 'Girl Scout', 'Pikachu', 'Spongebob', 'Baby Yoda', 'Pilgrim', 'Cinderella', 'Baker', 'Lincoln', 'Thief', 'Leprechaun', 'Harry Potter', 'Shrek', 'Yoshi', 'Queen Elizabeth', 'Skip', 'Burp', 'Cook', 'Scratch', 'Sleep', 'Plant', 'Purchase', 'Text', 'Tie', 'Snore', 'Catch', 'Study', 'Olympics', 'Sandcastle', 'Recycle', 'Black hole', 'Applause', 'Blizzard', 'Sunburn', 'Time machine', 'Lace', 'Monday', 'Atlantis', 'Swamp', 'Panama', 'Canal', 'Sunscreen', 'Dictionary', 'Vanilla', 'Century']
#this are all the words that can be chosen

play_again = "yes"

while play_again == "yes":

    word = random.choice(word_bank)
    word_lower = word.lower()
    #this makes the word chosen completely random

    guessedWord = [' ' if char == ' ' else '_' for char in word]
    #makes the word "invisible" (_)

    attempts = 10
    #attempts to guess letters of the word before failure

    while attempts > 0:
        print('\nCurrent word: ' + ''.join(guessedWord))

        guess = input ('Guess a letter: ').lower()

        if guess in word_lower:
            for i in range(len(word_lower)):
                if word_lower[i] == guess:
                    guessedWord[i] = word[i]
            print('Great guess!')
        else:
            attempts -= 1
            print('Wrong guess! Attempts left: ' + str(attempts))

        if '_' not in guessedWord:
            print('\nCongratulations!!🎉 You guessed the word: ' + word)
            play_again = input('\nWant to play again? (yes/no): ').lower()
            break
            
        
    if attempts == 0 and '_' in guessedWord:
        print('\nYou\'ve run out of attempts! The word was: ' + word)
        
        play_again = input('\nWant to play again? (yes/no): ').lower()
    
    print("Thanks for playing!")



