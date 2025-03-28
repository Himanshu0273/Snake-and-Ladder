UC 3: The Player then checks for a Option. They are No Play, Ladder or Snake. 

Used "randint" function from "random" module in python to generate a number between 0 and 2 where,
0 represents No Play: player stays in the same position
1 represents Ladder: player moves ahead by the number of position received in the die
2 represents Snake: player moves behind by the number of positions received in the die

An alternate way of implementing this can be using choice function from the random module on a list with members: ['No Play', 'Ladder', 'Snake']
