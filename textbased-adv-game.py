def show_instructions():
    print("""
    \t\tWelcome to the Text Adventure Game!
    -----------------------------------------------------------
    Commands:
        \t"go [direction]" \t - Move to a new room (north, south, east, west)
        \t"get [item]" \t\t - Pick up an item from the room
        \t"inventory" \t\t - Show your current items
        \t"look" \t\t\t - Get details about the current room
        \t"exit" \t\t\t - Exit the game
    -----------------------------------------------------------
    """)

def show_room(room):
    print(f"\n\tYou are in the {room['name']}.")
    print(f"\t\"{room['description']}\"")
    if 'item' in room:
        print(f"\t...You notice a {room['item']} here...")

def main():
    # Room layout with spooky descriptions
    rooms = {
        'Hall': {
            'name': 'Hall',
            'description': 'The air feels cold, and shadows move on the walls as if they are alive. An unsettling silence fills the room.',
            'south': 'Kitchen',
            'east': 'Living Room',
            'item': 'shield'
        },
        'Kitchen': {
            'name': 'Kitchen',
            'description': 'The faint sound of dripping water echoes. The walls are stained, and the smell of something burnt lingers.',
            'north': 'Hall',
            'item': 'dagger'
        },
        'Living Room': {
            'name': 'Living Room',
            'description': 'An old, broken chandelier swings slightly even though there is no breeze. The furniture is covered in dust, and you feel like something is watching you.',
            'west': 'Hall',
            'south': 'Garden',
            'item': 'sword'
        },
        'Garden': {
            'name': 'Garden',
            'description': 'A thick mist clings to the ground, and the plants here seem overgrown and twisted. You can barely see, but strange shapes move in the fog.',
            'north': 'Living Room',
            'item': 'spear'
        }
    }

    # Game state
    inventory = []
    current_room = 'Hall'
    
    # Show game instructions
    show_instructions()

    # Main game loop
    while True:
        show_room(rooms[current_room])
        action = input("\n>> What do you want to do? ").strip().lower().split()

        if len(action) < 1:
            print("\tInvalid input, try again.")
            continue

        command = action[0]
        
        if command == 'go':
            if len(action) < 2:
                print("\tGo where?")
                continue
            direction = action[1]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print("\t...You move to another room...")
            else:
                print("\tYou can't go that way.")
        
        elif command == 'get':
            if len(action) < 2:
                print("\tGet what?")
                continue
            item = action[1]
            if 'item' in rooms[current_room] and rooms[current_room]['item'] == item:
                inventory.append(item)
                print(f"\tYou picked up a {item}.")
                del rooms[current_room]['item']  # Remove item from the room
            else:
                print(f"\tThere is no {item} here.")
        
        elif command == 'inventory':
            if inventory:
                print("\tYour inventory contains:", ", ".join(inventory))
            else:
                print("\tYour inventory is empty.")
        
        elif command == 'look':
            show_room(rooms[current_room])
        
        elif command == 'exit':
            print("\n\tThanks for playing! Goodbye!")
            break
        
        else:
            print("\tUnknown command. Type 'look' to check the room or 'inventory' to see what you have.")

if __name__ == "__main__":
    main()
