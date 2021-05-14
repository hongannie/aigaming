#!/usr/bin/env python
# coding: utf-8

# In[80]:


import numpy as np
def check_winner(matrix):  
    xpos = ''
    opos = ''
    
                #horizontal win patterns
    winnercombs = ["000000111","000111000","111000000",
                   #vertical win patterns
                   "100100100","010010010","001001001",
                   #diagonal win patterns
                   "100010001","001010100"]
    print(matrix)
    # traverse through all tictactoe squares
    for i in matrix:
        for j in i:
            if j == 'x':
                xpos += '1'
                opos += '0'
            elif j == 'o':
                xpos += '0'
                opos += '1'
            else:
                xpos += '0'
                opos += '1' 
    
    # convert to binary string
    #xpos = xpos.encode('ascii')
    #opos = opos.encode('ascii')

    for i in winnercombs:
        if i and xpos == i:
            print('Winner is X')
            return True
        elif i and opos == i:
            print('Winner is O')
            return True
    return False


# In[125]:


def single_player(board):
    
    #def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
        
    #if letter == 'X':
     #   return 'X'
    #else:
     #   return 'O'
    #return letter
    #inputPlayerLetter()

    def whoGoesFirst():
        if letter == 'X':
            print("Player will go first")
            return 'player'
        else:
            print("Computer will go first")
            return 'computer'
    #whoGoesFirst()
    
    def computerLetter():
        if letter == 'X':
            computerLetter = 'O'
        else:
            computerLetter = 'X'
        return computerLetter
    

    
    states = []
    lr = 0.2
    exp_rate = 0.3
    decay_gamma = 0.9
    states_value = {}
    
    boardpos = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], np.int32)
    print(boardpos)
    possible = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    turn = whoGoesFirst()
 ####   

    def availPos():
        position = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    position.append((i,j))
        return position
    
    def updateState(position):
        pos = position[pos-1]
        xx, xy = int(pos[0]), int(pos[1])
        board[xx][xy] = computerLetter
        board[position] = computerLetter
        
    def giveReward(self):
        result = self.winner()
        if result == 1:
            self.p2.feedReward(1)
            self.p2.feedReward(0)
        elif result == -1:
            self.p2.feedReward(0)
            self.p2.feedReward(1)
        else:
            self.p2.feedReward(0.1)
            self.p2.feedReward(0.5)
    
    def reset(self):
        self.board = np.zeros((rows,cols))
        self.boardHash = None
        self.end = False
        self.playerSymbol = 1


    def chooseAction(position,board,computerLetter):
        position = availPos()
        if np.random.uniform(0,1) <- exp_rate:
            xpos = np.random.choice(len(position))
            opos = np.random.choice(len(position))
            action = position[xpos][opos]
        else:
            value_max=-999
            for p in position:
                next_board = board.copy()
                next_board[p] = computerLetter
                next_boardHash = getHash(board)
                value = 0 if states_value.get(next_boardHash) is None else states_value.get(next_boardHash)
                if value >= value_max:
                    value_max = value
                    action = p
        return action
    
    def addState(state):
        states.append(state)
        
    def feedReward(reward):
        for st in reversed(states):
            if states_value.get(st) is None:
                states_value[st] = 0 
            states_value[st] += lr*(decay_gamma*reward - states_value[st])
            reward = states_value[st]
            
    def reset():
        states = []
        
    def savePolicy():
        fw = open('policy_' + str(name), 'wb')
        pickle.dump(states_value,fw)
        fw.close()
    
    def loadPolicy(file):
        fr = open(file,'rb')
        states_value = pickle.load(fr)
        fr.close()
    
####    
#check if the move is valid
def isValidMove(board_list,spot):
#only the input in the range of [0:8}, not occupied by x or o is valid
    if 0<= spot <= 8 and board_list[spot]!='x' and board_list[spot]!='o':
         print("True")

         return True
    else:
         print("Invaild. Enter another value.")
         return False


    
    while not check_winner(board):
        if turn == 'player':
            pos = int(input('Where do you want to place X? Insert a num val: '))
            pos = possible[pos-1]
            xx, xy = int(pos[0]), int(pos[1])
            board[xx][xy] = letter
            turn = 'computer'
        else:
            positions = availPos()
            action = chooseAction(positions,board,computerLetter)

            self.updateState(p2_action)
            #self.showBoard()
            #win = self.winner()
            #if win is not None:
             #   if win == -1:
              #      print(self.p2.name, "wins!")
               # else:
                #    print("tie!")
                #self.reset()
                #break

                
                
            
            
            
            #positions = availPos(board)
            #print(positions)
            #pos = positions[pos-1]
            #print(pos)
            #p1_action = chooseAction(positions,board,computerLetter())
            #updateState(p1_action)
            #turn = 'player'
                                     
                            
    
        


# In[126]:


def two_player(board):
    boardpos = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], np.int32)
    print(boardpos)
    possible = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    turn = 'x'
    
    while not check_winner(board):
        if turn == 'x':
            print('You are player 1. You will use X')
            pos = int(input('Where do you want to place X? Insert a num val: '))
            pos = possible[pos-1]
            xx, xy = int(pos[0]), int(pos[1])
            board[xx][xy] = turn
            turn = 'o'
            #check_winner(board)
            
        else:
            print('You are player 2. You will use O')
            pos = int(input('Where do you want to place O? Insert a num val: '))
            pos = possible[pos-1]
            xx, xy = int(pos[0]), int(pos[1])
            board[xx][xy] = turn
            turn = 'x'
            #check_winner(board)


# In[127]:


def tictactoe(players):
    assert(players <= 2)
    assert(players > 0)
    
    board = np.zeros((3,3), dtype=str)
    
    if players == 1:
        single_player(board)
    
    if players == 2:
        two_player(board)


# In[128]:


#two player tic tac toe simulation
#tictactoe(2)


# In[129]:


#one player tic tac toe simulation
tictactoe(1)


# In[ ]:




