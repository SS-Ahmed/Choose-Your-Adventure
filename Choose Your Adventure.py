name = input("Type your name: ")
print("Welcome", name, "to the beginning of this adventure!")

answer = input("You are tasked with a mission. You find yourself on what appears to be a barren, isolated island. Do you wish to proceed? ").lower()

if answer == "yes":
    answer = input("Wise desicion. You now have a choice to trek 10km to the base of a nearby mountain, or to walk for 5km to reach a spring. Do not be rash in your desicion, it may lead to your undoing. Type trek, or walk: ")

    if answer == "trek":
        print()
    elif answer == "walk":
        print()
    else:
        print("Not a valid option. You lose!")

elif answer == "no":
    print("Too bad ")      
else:
    print("Not a valid option! Well done, you played yourself.")