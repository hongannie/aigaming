# AI Gaming
**AI Gaming: Dynamic Programming (Algorithms Project)**

For our project, we will model a tic-tac-toe game as a Markov decision process and solve it using dynamic programming. The AI will compute the best action to take against in response moves made by the user via Bellman's principle of optimality. The Bellman equation is one of the basic methods of solving reinforcement learning

https://en.wikipedia.org/wiki/Bellman_equation

To start off, we will have to break down the process into several steps.  We have to determine several aspects of the game: the set of states S, the set of actions A, and the set of rewards R. At each time step (t = 0, 1, 2 ...), the AI receives the state St and selects an action At. The state-action pair (St, At) yields a new state St+1 and reward R at t+1. This will be modeled as a markov decision process.

To implement this project through code, we anticipate a tripart effort. We need 1) a (python) program that implements the tic-tac-toe game between a player and the AI, 2) a (python) program that implements the AI strategy, 3) a visualization of the simulation (javascript and html). For the implementation of the game board, we plan to use an array to keep track of the moves of the user and the AI. For the Markov decision process, we plan to use a list of size 3, or triples, that describe all the possible combinations.
