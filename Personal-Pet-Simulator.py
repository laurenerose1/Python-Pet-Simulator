# This is a pick your own adventure type of similuator where you get to create your own pet, play with it, get new toys etc.
# create different pet type options

# pet dictionary
pet = {"name": "", "type": "", "age": 0, "hunger": 0, "toys": []}

# option to quit game
def quitSimulator():
    print("Quit the pet simulator. Thanks for playing")
# feed your pet- decrease hunger
def feedPet():
    newHunger = pet["hunger"] - 20
    if newHunger < 0:
        newHunger = 0
    pet["hunger"] -= 20
    print("You have fed your pet, decreasing hunger by 10!")

# pet toys data object
petToys = {"cat": ["cat nip", "plush mouse", "string"], "dog": ["ball", "plush toy", "bone"], "turtle": ["shell", "castle", "floating deck" ], "rabbit": ["tunnel", "ball", "stick"]}

# Get pet new toy
def getToys():
    print("Yay!! Let's get new toys!")
    toyOptions = petToys[pet["type"]]
  
    toyNum = -1

    while toyNum < 0 or toyNum >= len(toyOptions) - 1:
        for i in range(len(toyOptions)):
            print(str(i) + ": " + toyOptions[i])
        toyNum = int(input("Input the number of the toy you would like: " ))

    chosenToy = toyOptions[toyNum]
    pet["toys"].append(chosenToy)
    print ("Cool! You selected the " + chosenToy + "!")

    # Pet Plays with toys
def playToys():
    print(pet["name"] + "had a wonderful time playing with toys!")

# print menu
def printMenu(menuOptions):
  print()
  print("Here is the current menu of options you have:")
  print("----------")

  # iterate through the menu options, printing out the key meant to be pressed, along with its corresponding text
  for key in menuOptions:
    print(key + ":\t" + menuOptions[key]["text"])

  # print an additional newline character
  print()

#current pet stats 
def printStats():
    print("Your " +pet["type"] + pet["name"] + " is doing great!!")
    print ("Your pet currently has: " + str(len(pet["toys"])) + ", which are: ")
    for toy in pet["toys"]:
        print(toy)
    print("Your pet's hunger level currently is: " + str(pet["hunger"]) + "of a max 100.")
    print("Your pet is" + str(pet["age"]) + "days old.")
    print()

# Pick your pet prompt
def initPet(petToys):
# Extract the possible pets into a list for easier references
    petOptions = list(petToys.keys())

  # Initialize selectedPet in order to continue prompting for pets if choice given wasn't in the dictionary
    selectedPet = ""

  # Loop through pets
    while selectedPet not in petOptions:
        print("Your options of pets are: ")
        for option in petOptions:
            print(option)
    
        selectedPet = input("Please select one of these pets. Which one would you like? ")

        if selectedPet not in petOptions:
            print("Sorry! That wasn't one of our options. Try again")
  # Store pet type in dictionary
    pet["type"] = selectedPet

    #name your pet
    pet["name"] = input("What do you want to name your " + pet["type"] + "? ")
  

# main game loop
def main():
    #initialize our pet
    initPet(petToys)

    menuOptions = {"Q": { "function": quitSimulator, "text": "Quit the game"}, "F": { "function": feedPet, "text": "Feed " + pet["name"] + "!"}, "G": { "function": getToys, "text": "Get a toy for " + pet["name"] + "!"}, "P": { "function": playToys, "text": "Play with " + pet["name"] + " and your toys!"} }
    # print the menu of options
    keepPlaying = True
    while keepPlaying:
        menuSelection = ""
## get input from players & validate
    while menuSelection not in menuOptions.keys():
        printMenu(menuOptions)
        menuSelection = input("Which of these menu options would you like to use? ").upper()

    # user can quit using Q
    if menuSelection == "Q":
        keepPlaying = False

    menuOptions[menuSelection]["function"]()

#increase pet's hunger
    pet["hunger"] += 10
    pet["age"] += 1

    printStats()


    main()