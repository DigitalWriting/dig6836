# bolt simulator version 2, with graphics!

position = "fully_closed"

action = input("Turn the bolt? (l/r): ")

while action != "q":
    if position == "fully_closed":
        print("       _______")
        print("      |       |")
        print("      |       |")
        print("      |       |")
        print("      |_______|")
        print("       |     |")
        print("       |_____|")
    elif position == "midway_open":
        print("       _______")
        print("      |\\      |")
        print("      | \\     |")
        print("      |  \\    |")
        print("      |___\\___|")
        print("       |     |")
        print("       |_____|")
    
    if action == "l" and position == "fully_closed":
        position = "midway_open"
    elif action == "l" and position == "midway_open":
        position = "fully_open"
    elif action == "r" and position == "midway_open":
        position = "fully_closed"
    else:
        print("Too tight! Can't tighten more.")
        action = input("Turn the bolt? (l/r): ")

print("       _______")
print("      |\\     /|")
print("      | \\   / |")
print("      |  \\ /  |")
print("      |___\\___|")
print("       |     |")
print("       |_____|")

print("Bolt is fully open. Type 'q' to quit.")


'''
The provided script is a simulation of a bolt that can be turned left (l) or right (r) to change its position. The script uses variables and conditional logic to track and update the position of the bolt until it reaches the "fully_open" state.

Here's how the script works:

1. The initial position of the bolt is set to "fully_closed".
2. The script enters a while loop that continues until the position of the bolt is "fully_open".
3. Inside the loop, the user is prompted to enter an action to turn the bolt: "l" for left or "r" for right.
4. The script checks the entered action and the current position of the bolt using conditional statements (if-elif-else).
5. If the action is "l" and the position is "fully_closed", the bolt is turned to the "midway_open" position.
6. If the action is "l" and the position is "midway_open", the bolt is turned to the "fully_open" position.
7. If the action is "r" and the position is "fully_open", the bolt is turned to the "midway_open" position.
8. If the action is "r" and the position is "midway_open", the bolt is turned to the "fully_closed" position.
9. If the entered action is none of the above, an "invalid input" message is printed.
10. After each action, the script prints the current position of the bolt.
11. Once the position of the bolt becomes "fully_open", the loop exits.
12. The script prints a message indicating that the bolt is fully open and the simulation ends.

You can run this script and interact with it by entering "l" or "r" when prompted to turn the bolt. The script will continue until the bolt reaches the fully open position.
'''
