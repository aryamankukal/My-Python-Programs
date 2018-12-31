films = {
    "Finding Dory" : [3,5],
    "Bourne" : [18,5],
    "Tarazan" : [15, 5],
    "Ghost Busters" : [12, 5]
    }
# Test
while True:
    choice = input("What movie would you like to watch?").strip().title()

    if choice in films:
        age = int(input("How old are you?").strip())

        if age >= films[choice][0]:


            if films[choice][1] > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
                print("There are" , films[choice][1] , "tickets left for this movie!")
            else:
                print("Sorry! We're sold out!")
        else:
            print("You're too young to see that film ")

    else:
        print("I'm sorry. We don't have that film")
        print("Perhaps you're at the wrong theater")