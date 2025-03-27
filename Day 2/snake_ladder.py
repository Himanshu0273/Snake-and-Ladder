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
        return new_pos
    
    else:  # Snake
        new_pos = pos - steps
        if new_pos < 0:
            print(f"You got Snake! You rolled {steps}, but can't go below 0. Restarting at 0.\n")
            return 0
        else:
            print(f"You got Snake! You move back {steps} steps.\nStarted at: {pos}")
            return new_pos
        
# UC5: Ensure the player reaches exactly 100 to win
def check_win_condition(pos):
    if pos > 100:
        print(f"You rolled too high! Staying at {pos - (pos - 100)} until you roll exactly {100 - (pos - (pos - 100))}.\n")
        return pos - (pos - 100)
    return pos

# UC6: Report the number of dice rolls and positions after every roll
def report_dice_roll(player, rolls):
    print(f"{player} has rolled {rolls} times. Current Position: {player}\n")
    

#UC7: Game is played between 2 players

def play_game():
    player_A = start()
    player_B = start()
    dice_count_A = 0
    dice_count_B = 0

    while player_A != 100 and player_B != 100:
        print("Player A MOVES:")
        player_A = move(player_A)
        player_A = check_win_condition(player_A)
        dice_count_A += 1
        report_dice_roll("Player A", dice_count_A)

        if player_A == 100:
            print(f"HOORAY!!! Player A WINS in {dice_count_A} dice rolls!")
            break

        print("Player B MOVES:")
        player_B = move(player_B)
        player_B = check_win_condition(player_B)
        dice_count_B += 1
        report_dice_roll("Player B", dice_count_B)

        if player_B == 100:
            print(f"HOORAY!!! Player B WINS in {dice_count_B} dice rolls!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
