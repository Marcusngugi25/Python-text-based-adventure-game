print("Welcome to the game!")
name = input("Insert your name: ")
age = int(input("Insert your age: "))

print("Hello", name, "You are", age, "years old.")

health_points = 50 

if age >= 18:
    print("You are old enough to play!")

    want_play = input("Do you want to play? ").lower()
    if want_play == "yes":
        print("Welcome, let's play!")
        print("You are starting with ", health_points, "health points.")

        left_or_right = input("Do you want to go left or right (left/right)? ")
        if left_or_right == "left":
            answer = input("You walk 50 steps towards the river. Do you use the bridge or swim across (bridge/swim)? ")

            if answer == "bridge":
                print("The bridge crumbles when you start walking across it, a crocodile attacks you and you die. Game lost! ")

            else:
                path = input("You swim across to the other side. Do you go to the waterfall or to the cave (waterfall/cave)? ")

                if path == "waterfall":
                    print("You reached the waterfall and found a pond full of fish. Next to the pond is a big chest full of gold. You win the game! ")

                elif path == "cave":
                    c_w = input("You enter the cave and are bitten by a bat. You lose 20 health. You see two objects on the ground. Do you pick up the torch or the axe (torch/axe)? ")
                    health_points -= 20

                    if health_points <= 0:
                        print("You lost all your health points. Game lost. ")
                    else:
                            print("You are still alive! Keep playing!")

                    if c_w == "torch":
                        print("You switch on the torch and a swarm of bats attack you. You lose 20 health points but get out of the cave. ")
                        health_points -= 20

                        if health_points <= 0:
                            print("You lost all your health points. Game lost. ")
                        else:
                            print("You are still alive! Keep playing!")
                    elif c_w == "axe":
                        print("You use the axe to pick at the back of the cave. You create an opening and get out of the cave. You find a path that takes you to the waterfall. You reached the waterfall and found a pond full of fish. Next to the pond is a big chest full of gold. You win the game! ")

                    else:
                        print("You lost the game.")    
                else:
                    path = input("You get out of the cave. Do you go to the waterfall or into the forest (waterfall/forest)? ")

                    if path == "forest":
                        print("You go to the forest and get bitten by a snake. You lose 10 health points.")
                        health_points -= 10

                        if health_points <= 0:
                            print("You lost all your health points. Game lost. ")
                        else:
                            print("You are still alive! Keep playing!")

                    elif path == "waterfall":
                        print("You reached the waterfall and found a pond full of fish. Next to the pond is a big chest full of gold. You win the game! ")

                    else:
                        print("You lost the game.")
                    
        else:
            print("You fell down a hole and died. Game lost!")

    else:
        print("Goodbye, see you next time!")

else:
    print("You can not play this game. You are too young!")