def display_menu():
    print("\n" + "="*40)
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("="*40)

def add_item(shopping_list):
    item = input("Enter the item to add: ")
    if item:
        shopping_list.append(item)
        print(f"'(item)' has been added to the shopping list.")
    else:
        print("Please enter a valid item.")

def remove_item(shopping_list):
    if not shopping_list:
        print("The shopping list is empty. Nothing to remove.")
        return
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' is not in the shopping list.")

def view_list(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Current Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
        print(f"Total items: {len(shopping_list)}")

def main():
    shopping_list = []
    while True:
        display_menu()

        try:
            choice = input("Enter your choice (1-4):").strip()
            if choice == "1":
                add_item(shopping_list)
            elif choice == "2":
                remove_item(shopping_list)
            elif choice == "3":
                view_list(shopping_list)
            elif choice == "4":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
