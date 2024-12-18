# INST126
All my work from INST126
# INST126
Tuple Out Game
Brian McDowell

How to Play:
1. run the code
2. the dye will automatically roll for player 1 
3. You will be asked if you would like to roll again enter either yes or no.
4. if you choose to roll again you may keep rolling until tupled out or you are at a score you are satisfied with and you respond no.
5. After your turn your score will be calculated and displayed for all players to see
6. Player 2's dye will be automatically rolled once player 1's turn ends.
7. Player 2 will be faced with the same decisions as player 1 (yes or no)
8. Once the first player reaches a score of 30 or more the game will end. 

Further explanation:
The Tuple Out Game is a dice game for two players based on strategy and chance. Players roll 3 dice each turn, if 2 of the dye land on the same number these dices are "locked in" meaning your stuck with a 4 and a 4 for example. Lets say you roll a 1 on your third dye and choose to reroll that dye to improve your score, if you land on a 4 you are "tupled out" meaning you get 0 points that round. If you land on any other number that isnt a 4 you can either choose to roll again or stay and take the points you earned that round.

Since the first draft of my program, I have changed the following:
1. The user will be prompted to set the target score
2. The user will be prompted to play again if they would like
3. There is a win counter that counts the amount of games won

4. Example game:
5. Player 1 wins the game with 20 points!

Current win count:
Player 1: 1 wins
Player 2: 0 wins
Do you want to play again?yes
Enter the Target Score:20

Player 1's total score: 0

Player 1's turn:
Rolling 3 dice...
Initial roll: [6, 6, 5]
Fixed dice: [6, 6], Unfixed dice: [5]
Do you want to reroll the unfixed dice? (yes/no): no
Keeping the unfixed dice as: [5]
Final dice: [6, 6, 5]
Total score this turn: 17
Player 1's updated score: 17

Player 2's total score: 0

Player 2's turn:
Rolling 3 dice...
Initial roll: [1, 2, 4]
No dice match, no fixed dice.
Fixed dice: [], Unfixed dice: [1, 2, 4]
Do you want to reroll the unfixed dice? (yes/no): no
Keeping the unfixed dice as: [1, 2, 4]
Final dice: [1, 2, 4]
Total score this turn: 7
Player 2's updated score: 7

Player 1's total score: 17

Player 1's turn:
Rolling 3 dice...
Initial roll: [2, 3, 1]
No dice match, no fixed dice.
Fixed dice: [], Unfixed dice: [2, 3, 1]
Do you want to reroll the unfixed dice? (yes/no): no
Keeping the unfixed dice as: [2, 3, 1]
Final dice: [2, 3, 1]
Total score this turn: 6
Player 1's updated score: 23

Player 1 wins the game with 23 points!

Current win count:
Player 1: 2 wins
Player 2: 0 wins
Do you want to play again?no

Thanks for playing!
Player 1: 2 wins
Player 2: 0 wins

The game Lasted 2 minutes 24 seconds!

(base) brianmcdowell@Brians-MacBook-Pro-5 INST126 % 
