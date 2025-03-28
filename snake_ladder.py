from random import randint

# UC 1: Start the game at 0
def start():
    return 0

# UC 2: Roll the die (1-6)
def rolldie():
    return randint(1,6)

# UC 3: Determine play type 
# (0: No Play, 1: Ladder, or 2: Snake)
def moveToPlay():
    return randint(0,2)


#UC 4: Move until you reach 100, the least value the player can have is 0
def move(pos):
    movetype = moveToPlay()
    steps = rolldie()
    
    if movetype == 0: #No Play
        print("You got NO PLAY!!Wait for the next turn")
    
    elif movetype == 1: #Ladder
        print(f"You got Ladder! You move forward {steps} steps.\nStarted From: {pos}")
        new_pos = pos + steps
        print(f"Ended at: {pos}")        
        return new_pos
    
    else:  # Snake
        new_pos = pos - steps
        if new_pos < 0:
            print(f"You got Snake! You rolled {steps}, but can't go below 0. Restarting at 0.\n")
            return 0
        else:
            print(f"You got Snake! You move back {steps} steps.\nStarted at: {pos}\nEnded at: {new_pos}")
            return new_pos