Snake and Ladder - Two Player Game

Overview:
This program simulates a two-player Snake and Ladder game, where players take turns rolling a die and moving based on game rules until one reaches exactly 100.  

Features:
- Turn-based gameplay: Two players (Player A & Player B) start from position 0.  
- Rolling a die (1-6): Determines how many steps a player moves.  
- Move type decision: Players encounter No Play (0), a Ladder (1) to move forward, or a Snake (2) to move backward.  
- Win condition enforcement: Players must reach exactly 100 to win. If they exceed 100, they remain at the previous position.  
- Game status updates: The program tracks and displays player positions and dice roll counts after every turn.  

How to Play: 
1. Run the script to start the game.  
2. Players take turns rolling the die and moving according to game rules.  
3. The game continues until one player reaches exactly 100.  
4. The winner is announced, along with the number of dice rolls taken.  

Usage:
To execute the game, run the script:  
bash:
python snake_and_ladder.py

Dependencies:
- Python 3.x  
- Random module (`randint`) for die rolls and move type selection  
