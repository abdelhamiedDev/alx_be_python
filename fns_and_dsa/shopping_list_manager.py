def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            added_item = input("Enter the item to add: ")
            shopping_list.append(added_item)
            print(f"{added_item} has been added to the shopping list.")

        elif choice == '2':
            # Prompt for and remove an item
            removed_item = input("Enter the item to remove: ")
            if removed_item in shopping_list:
                shopping_list.remove(removed_item)
                print(f"{removed_item} has been removed from the shopping list.")

            else:
                print("Item not found in the shopping list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f" - {item}")
            else:
                print("The shopping list is empty.")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()