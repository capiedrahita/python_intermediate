
# Inventory Management
# This program allows users to manage an inventory interactively.

# Step 1: Initialize the inventory
inventory = {}

# Step 2: Define the menu
def show_menu():
    print("\nOptions:")
    print("[1] Add item")
    print("[2] Remove item")
    print("[3] View inventory")
    print("[4] Exit")

# Step 3: Handle user actions
while True:
    show_menu()
    choice = input("Choose an option: ").strip()
    
    if choice == "1":
        item = input("Enter the item name: ").strip()
        quantity = int(input("Enter the quantity: "))
        inventory[item] = inventory.get(item, 0) + quantity
        print(f"Added {quantity} {item}(s) to the inventory.")
    elif choice == "2":
        item = input("Enter the item name to remove: ").strip()
        if item in inventory:
            del inventory[item]
            print(f"Removed {item} from the inventory.")
        else:
            print(f"{item} is not in the inventory.")
    elif choice == "3":
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    elif choice == "4":
        print("Exiting inventory management. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
