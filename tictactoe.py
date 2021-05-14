# -*- coding: utf-8 -*-

"""
Created on Thu Apr 29 23:05:47 2021

@author: annie
"""
import numpy as np
import pickle

isEnd = False

def check_winner(matrix):  
    xpos = ''
    opos = ''
    allpos = ''
    
                #horizontal win patterns
    winnercombs = [b'000000111',b'000111000',b'111000000',
                   #vertical win patterns
                   b'100100100',b'010010010',b'001001001',
                   #diagonal win patterns
                   b'100010001',b'001010100']
    print(matrix)
    # traverse through all tictactoe squares
    for i in matrix:
            for j in i:
                if j == 'x':
                    xpos += '1'
                    opos += '0'
                    allpos += '1'
                elif j == 'o':
                    xpos += '0'
                    opos += '1'
                    allpos += '1'
                else:
                    xpos += '0'
                    opos += '0' 
    
    # convert to binary string
    xpos = xpos.encode('ascii')
    opos = opos.encode('ascii')
    allpos = allpos.encode('ascii')

    for i in winnercombs:
        if i and xpos == i:
            print('Winner is X!')
            return 1
        elif i and opos == i:
            print('Winner is O!')
            return -1
    
    #check if board is full
    if allpos == b'111111111':
        print("It's a draw!")
        return 'draw'
        
def tictactoe():
    players = int(input('How many players? Enter 1 or 2: '))
    assert(players <= 2)
    assert(players > 0)
    
    board = np.zeros((3,3), dtype=str)
    
    if players == 1:
        single_player(board)
    
    if players == 2:
        two_player(board)
        
def single_player(board):
    
    possible = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    symbol = 'x'
    
    #load training policy1
    fr = open("policy_p1",'rb')
    p1states_value = pickle.load(fr)
    fr.close()
    
    #load training policy2
    fr = open("policy_p2",'rb')
    p2states_value = pickle.load(fr)
    fr.close()
    
    def availablePlays(matrix):
        position = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    position.append((i,j))
        return position
    
    def chooseAction(positions, current_board, symbol, player):
        exploration_rate = 0.3
        #make a random move
        if np.random.uniform(0, 1) <= exploration_rate:
            pos = np.random.choice(len(positions))
            action = positions[pos]
        else:
            value_max = -999
            action = positions[0]
            for p in positions:
                boardcopy = current_board.copy()
                boardcopy[p] = symbol
                boardcopy_hash = getHash(boardcopy)
                if player == 'p1':
                    value = 0 if p1states_value.get(boardcopy_hash) is None else p1states_value.get(boardcopy_hash)
                else:
                    value = 0 if p2states_value.get(boardcopy_hash) is None else p2states_value.get(boardcopy_hash)
                if value >= value_max:
                    value_max = value
                    action = p
        return action
    
    def getHash(matrix):
        matrixHash = str(matrix.reshape(9))
        return matrixHash
    
    def updateState(matrix, position, player):
        nonlocal symbol
        if player == 'p1':
            symbol = 'o'
            matrix[position] = 'x'
        else:
            symbol = 'x'
            matrix[position] = 'o'
            
    def goesFirst():
        order = int(input('Would you like to go first or second? Enter 1 or 2' ))
        if order == 1:
            return 1
        else:
            return 2

    while not isEnd:
        
        # Player 1  
        positions = availablePlays(board)
        p1_action = chooseAction(positions, board, symbol, 'p1')       
        updateState(board, p1_action, 'p1')        
        win = check_winner(board)
        if win is not None:
            break

        else:
            # Player 2
            print('You are player 2. You will use O')
            pos = int(input('Where do you want to place O? Insert a num val: '))
            pos = possible[pos-1]
            xx, xy = int(pos[0]), int(pos[1])
            board[xx][xy] = symbol
            playSymbol = 'x'
            win = check_winner(board)
            if win is not None:
                break

def two_player(board):
    boardpos = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], np.int32)
    print(boardpos)
    possible = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    turn = 'x'
    
    while not isEnd:
        if turn == 'x':
            print('You are player 1. You will use X')
            pos = int(input('Where do you want to place X? Insert a num val: '))
            pos = possible[pos-1]
            xx, xy = int(pos[0]), int(pos[1])
            board[xx][xy] = turn
            turn = 'o'
            win = check_winner(board)
            if win is not None:
                break
            else:
                print('You are player 2. You will use O')
                pos = int(input('Where do you want to place O? Insert a num val: '))
                pos = possible[pos-1]
                xx, xy = int(pos[0]), int(pos[1])
                board[xx][xy] = turn
                turn = 'x'
                win = check_winner(board)
                if win is not None:
                    break
    
#two player tic tac toe simulation
tictactoe()

    