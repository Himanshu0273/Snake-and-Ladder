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