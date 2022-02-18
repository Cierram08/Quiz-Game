print("hello")

playing = input("Do you want to play my game? " )
if playing == "yes":
    game = input("Great! What do you do for a living? ")
    print("Sounds interesting. I hope you enjoy it.")
else:
    game = input("No problem. I hope you have a great day.")
    quit()
    
name = input("I didn't get your name? ")
print("Well," + " " + name + "," + " " + "nice to meet you.")

location = input("Where ya from? ")
print("Oh I would love to visit" + " " + location + " " + "one day.")

food = input("What's the best food there? ")
print("Yikes, I'm allergic to" + " " + food + ".")

food2 = input("Is" + " " + location + " " + "known for anything else? ")
print("Okay, that's more like it!")

tv_show = input("Do you watch TV? ")
if tv_show != "yes":
    print("I get it. No one really does anymore.")
    youtube = input("Youtube? ")
    if youtube == "yes":
        print("You can find almost anything on YouTube. I love it.")
    else:
        print("Sounds like you may spend your time more wisely than most.")
else:
    tv_show = input("What's your favorite show? ")
    print("Okay I keep hearing so much about" + " " + tv_show + "." + " " + "I have to check it out soon.")

siblings = input("Do you have siblings? (yes/no) ")
if siblings == "yes":
    how_many = input("Same. How many? ")
    print("Awesome. It's nice having siblings. (Most of the time ;))")
else:
    print("That's okay. I'm sure being an only child had its benefits.")

print("Well, it was nice getting to know you. I hope we can continue this sometime.")