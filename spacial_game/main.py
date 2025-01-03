print('''
*******************************************************************************
          _..._
        .'     '.      _     _
       /    .-""-\   _/ \~~~/ \_
     .-|   /:.   |  \_/_\_/_\_/
     |  \  |:.   /-_ _\\ |_| //
     | .-'-;:__.'   (_)   (_)
     .'=  *=|NASA|____|____|____
    /   _.  |     [ ]     |    .
   ; .'     '-.._  |  [ ] |   _.'
  / '   .--.    -=;_______;=-'
 /'    (    '.    
         '--' 

*******************************************************************************
''')

print("WELCOME TO THE GALACTIC EXPEDITION")
print("Your mission is to find the lost civilization in the Andromeda galaxy.")

# Initialize inventory
inventory = []

# First decision
direction = input(
    "You are approaching a wormhole. Do you want to enter or bypass it? Type 'enter' or 'bypass': ").lower()
if direction == "enter":
    print("You emerge on the other side in an unknown sector of space.")
    print("Your scanners detect a derelict spaceship nearby.")
    action_1 = input("Do you want to 'investigate' the spaceship or 'ignore' it? ").lower()

    if action_1 == "investigate":
        print("You find advanced alien tech on board. It's a shielding device!")
        inventory.append("shielding device")
    else:
        print("You bypass the spaceship and continue your journey.")

    # Second decision
    action_2 = input(
        "Your sensors detect a planet emitting faint signals. Do you 'land' to investigate or 'orbit' to observe? ").lower()
    if action_2 == "land":
        print("You land safely and discover ancient ruins with inscriptions.")

        # Third decision with inventory consideration
        action_3 = input(
            "The inscriptions show three paths: one to a 'temple', one to a 'cave', and one to a 'field'. Which one do you choose? ").lower()
        if action_3 == "temple":
            print("Inside the temple, you find a mysterious energy barrier.")
            if "shielding device" in inventory:
                print(
                    "You use the shielding device to bypass the barrier and discover the remnants of an advanced civilization. You WIN!")
            else:
                print("The barrier disintegrates your ship. You lose.")
        elif action_3 == "cave":
            print("The cave is dark and unstable.")
            print("You find rare artifacts and clues about the lost civilization. You WIN!")
        else:
            print("The field is vast and desolate. You find nothing and run out of supplies. You lose.")
    else:
        print("While orbiting, a rogue asteroid damages your ship.")
        if "shielding device" in inventory:
            print("The shielding device protects your ship. You continue your journey!")
        else:
            print("Without protection, your ship is destroyed. You lose.")
else:
    print("You bypass the wormhole but encounter hostile alien ships. You lose.")
