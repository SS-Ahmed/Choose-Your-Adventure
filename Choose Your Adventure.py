name = input("Type your name: ")
print("Welcome", name, "to the beginning of this adventure!")

answer = input("You are tasked with a mission. You find yourself on what appears to be a barren, isolated island. Do you wish to proceed? ").lower()

if answer == "yes":
    answer = input("Wise desicion. You now have a choice to trek 10km to the base of a nearby mountain, or to walk for 5km to reach a spring. Do not be rash in your desicion, it may lead to your undoing. Type trek, or walk: ")

    if answer == "trek":
        print("You trekked for 10 kilometres over a period of 2 hours and reached your destination. However, your hunger and thirst is increasing. The base of the mountain has a cave. You are provided with two options, either scaling the mountain, or exploring the cave, in search of resources. Type 'search' to scale the mountain, or type 'explore' to enter the cave: ")
    elif answer == "walk":
        print()
    else:
        print("Not a valid option. You lose!")

elif answer == "no":
    answer = input("Too bad. You don't have a choice. Either 'walk' the landscape, or try your luck and 'swim' away from the island: ")      

    if answer == "walk":
        print("You trekked for 10 kilometres over a period of 2 hours and reached your destination. However, your hunger and thirst is increasing. The base of the mountain has a cave. You are provided with two options, either scaling the mountain, or exploring the cave, in search of resources. Type 'search' to scale the mountain, or type 'explore' to enter the cave: ")
    elif answer == "swim":
        print("You swam towards a school of piranhas. You perished after 5 whole, painful minutes!")
    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option! Well done, you played yourself.")