name = input("Enter your name: ")
print("Welcome ", name, "to this awesome adventure ")

response = input("You are on rough road, it has a dead end and you choose either left or right. which route would you like to follow? ")

if response == "left":
    response = input("You just arrived at a river, you can walk thru or dive into the river? type walk to walk thru or type dive to dive into the river: ")

    if response == "walk":
        print("You just walk thru the river, congratulations")
    elif response == "dive":
        print("You just dive into the river and got eaten by a crocidile, you just lost the game")
    else:
        print("Try again😢")

elif response == "right":
    response = input("You just arrived at the bridge, it looks like a dead end, do you want cross it or headback (cross/back)? ")

    if response == "cross":
        response = input("You just crossed the bridge, you can now decide to move either to right or left(R/L)? ")

        if response == "R":
            print("You would meet a stranger and communicate with him ✔")
        elif response == "L":
            print("You just lost the game ❌")
        else:
            print("Try again next time ")
    
    elif response == "back":
        print("You headed back to the main road, that means you are heading home, this means you just lost the game")
    else:
        print("Try again😢")


else:
    print("Invalid option. You choose wrong try again😒")

print("Thanks for taking on this adventure ", name)