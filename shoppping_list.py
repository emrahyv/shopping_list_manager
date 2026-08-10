items = []


def get_choice():
    choice = (int(input('''Please enter one of the numbers below.
1. Add item.
2. Show list
3. Remove item
4. Exit

Choice : ''')))
    return choice

user_choice = get_choice()

while user_choice <= 4:
    
    if user_choice == 1:
        new_item = input("Enter new item : ")
        items.append(new_item)
        print("New item added to your shopping list successfully")
        user_choice = get_choice()
        
    elif user_choice == 2:
        print(items)
        user_choice = get_choice()
        
    elif user_choice == 3:
        
        if not items:
            print("The shopping list is empty.")
            user_choice = get_choice()
        if items:
            print(items)
            remove = input("Please enter the item that you want to remove: ")
        else:
            while remove not in items:
                print("This item doesn't exist.")
                print(items)
                remove = input("Please enter the item that you want to remove: ")
            else:
                items.remove(remove)
                print("Item has successfully removed from your shopping list")
                user_choice = get_choice()
        
        
    
    elif user_choice == 4:
        print("Goodbye!")
    
    else:
        print("Invalid choice. Please select a number from 1 to 4.")
