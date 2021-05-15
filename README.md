# AI Gaming
**AI Gaming: Dynamic Programming (Algorithms Project)**

The game has the option to play in 2 different modes: 
- Between two users
- Between a user and an AI agent

1. training.py → This is python code that trains the AIs to learn the best choice of action after multiple games based on a reward system. This code contains functions that simulates entire games between two AI agents. The method of reinforcement learning used is temporal difference learning. Each state has a value attached to it. Once the game is started, the agent computes all possible actions it can take in the current state and the new states that would result from each action. The states are collected in a states_value vector that contains values for all possible states in the games in a add_states function. The rewards are stored in the p1/2states_value dictionary. These updated states help the agent choose the best course of action based on the available positions after learning previously from prior games.

2. Tictactoe.py → This python code simulates the game based on the number of players. When the game is first initiated, it will ask the user to input the number of user players who will be playing. 
- Single player → This python code simulates a game between an AI agent and a user. This code takes input from the user who chooses either X or O. If the user chooses X, the user goes first. The simulation asks the user to select a position,represented by a number between 1-9, that they would like to mark their play. When the user makes a play, the AI agent will then use what it has learned from the training to choose a choice of action based that will provide the highest reward if possible. 
- Two player → This python code simulates a game between two users. The code will ask each user to select a number value representing the positions on the board where they would like to place a mark and switch turns after each action until someone wins. 
For the ‘human’ players, you enter where you want to put your symbol via this system:

