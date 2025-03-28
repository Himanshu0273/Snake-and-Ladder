UC 4: Repeat till the Player reaches the winning position 100. Note In case the player position moves below 0, then the player restarts from 0

Overview:
This function simulates a player's move in a Snake and Ladder game. It determines whether the player encounters a Ladder, Snake, or No Play based on the game rules.

Functionality: 
No Play (movetype = 0) → The player remains in the same position.

Ladder (movetype = 1) → The player moves forward by a random number of steps.

Snake (movetype = 2) → The player moves backward. If the move results in a position below 0, the player restarts at position 0.

Key Features
Uses moveToPlay() to determine the type of move.

Uses rolldie() to determine the number of steps moved.

Ensures that the player's position never falls below 0.
