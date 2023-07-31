 
items = []
item = input("Enter an item('STOP' to quit):").capitalize()

while item.upper() != 'STOP':
    
    # Add the item to the list
    items.append(item)
    
    if len(items) == 1:
        print('You have 1 item')
    else:
        print(f"You have {len(item)} items")
    
    # Ask for the  next item
    item = input("Enter an item('STOP' to quit):").capitalize()
    
    # Check if it is already in the list
    while item in items:
        print('Error:', item, 'already entered.')
        item = input('Enter another item:').capitalize()
        
    # Display the inventory if items
    num = 1
    for item in items:
        print(f" str(num). {item}") 
    num += 1