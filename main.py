#Uses objects instead of dictionaries

from pet import Pet, CuddlyPet, Toy

pets = []

main_menu = [   
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Give a toy to all your pets",
    "Do nothing",
]

def print_menu_error():
    print("That was not a valid choice. Try again.\n\n\n")    

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    choice_string += "***Please choose an option:***"
    return choice_string

def get_user_choice(choice_list):
    choice = -1
    choice_string = choices_to_string(choice_list)
    while choice == -1:
        try:
            choice = int(input(choice_string))
            if choice <= 0 or choice > len(choice_list):
                raise ValueError
        except ValueError:
            print_menu_error()
    return choice

def transition():
    pause = input("\n\nPress any key to continue")
    print("\033c")

adoption_menu = [
    "Pet",
    "Cuddly Pet"
]

def main():    
    print("\033c")
    while True:
        choice = get_user_choice(main_menu)
        
        if choice == 1:
            pet_name = input("What would you like to name your pet? ")
            print("Please choose the type of pet: ")
            type_choice = get_user_choice(adoption_menu)
            if type_choice == 1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(CuddlyPet(pet_name))
            print("You now have %d pets" % len(pets))
            transition()

        if choice == 2:
            for pet in pets:
                pet.get_love()
                print("All your pets are now a little happier!\n")
            transition()

        if choice == 3:
            for pet in pets:
                pet.eat_food()
                print("All your pets are now a little more full!\n")
            transition()

        if choice == 4:
            if pets != []:
                for pet in pets:
                    print(pet)
            else: 
                print("You don't have any pets right now.\n")
            transition()

        if choice == 5:
            for pet in pets:
                pet.get_toy(Toy())
                print("You gave all your pets a toy!\n")
            transition()

        if choice == 6:
            for pet in pets:
                pet.be_alive()
            transition()
main()
