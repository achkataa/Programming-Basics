riddle = ""
chances = 3
level = 1
word_list = ["Hello", "Name", "Clothes", "Kid", "Summit", "Brain"]
for word in word_list:
    if word == "Hello":
        print(f"Level {level}")
        riddle = "The word you use to greet someone"
        print(riddle)
        player_word = input()
        if player_word == word:
            print("You Guessed the word")
            print(f"You move to level {level + 1}")
        else:
            print("You didn't guess the word ")
            chances = chances - 1
            print(f"You have {chances} more chances")
            if chances == 0:
                print("Game over")
                break
    if word == "Name":
        riddle = "The word that a person,thing or place is known by"
        print(riddle)
        player_word = input()
        if player_word == word:
            print("You Guessed the word")
            print(f"You move to level {level + 2}")
        else:
            print("You didn't guess the word ")
            chances = chances - 1
            print(f"You have {chances} more chances")
            if chances == 0:
                print("Game over")
                break
    elif word == "Clothes":
        riddle = "Things that you wear to cover your body"
        print(riddle)
        player_word = input()
        if player_word == word:
            print("You Guessed the word")
            print(f"You move to level {level + 3}")
        else:
            print("You didn't guess the word ")
            chances = chances - 1
            print(f"You have {chances} more chances")
            if chances == 0:
                print("Game over")
                break
    elif word == "Kid":
        riddle = "Young person"
        print(riddle)
        player_word = input()
        if player_word == word:
            print("You Guessed the word")
            print(f"You move to level {level + 4}")
        else:
            print("You didn't guess the word ")
            chances = chances - 1
            print(f"You have {chances} more chances")
            if chances == 0:
                print("Game over")
                break
    elif word == "Summit":
        riddle = "The top of a mountain"
        print(riddle)
        player_word = input()
        if player_word == word:
            print("You Guessed the word")
            print("Congarts!You won the game")
        else:
            print("You didn't guess the word ")
            chances = chances - 1
            print(f"You have {chances} more chances")
            if chances == 0:
                print("Game over")
                break

#print(riddle)




