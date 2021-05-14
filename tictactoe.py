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
            print('Winner is X')
            return 1
        elif i and opos == i:
            print('Winner is O')
            return -1
    
    #check if board is full
    if allpos == b'111111111':
        print('Board is full')
        return 'full'
        
def tictactoe(players):
    assert(players <= 2)
    assert(players > 0)
    
    board = np.zeros((3,3), dtype=str)
    
    if players == 1:
        single_player(board)
    
    if players == 2:
        two_player(board)
        
def single_player(board):
    
    possible = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    playerSymbol = 'x'
    
    #open policy1
    fr = open("policy_p1",'rb')
    p1states_value = pickle.load(fr)
    fr.close()
    
    #open policy1
    fr = open("policy_p2",'rb')
    p2states_value = pickle.load(fr)
    fr.close()
    
    def availablePositions(matrix):
        position = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    position.append((i,j))
        return position
    
    def chooseAction(positions, current_board, symbol, player):
        exp_rate = 0.3
        #print('current',current_board)
        if np.random.uniform(0, 1) <= exp_rate:
            # take random action
            idx = np.random.choice(len(positions))
            action = positions[idx]
        else:
            value_max = -999
            action = positions[0]
            for p in positions:
                #print(p)
                boardcopy = current_board.copy()
                boardcopy[p] = playerSymbol
                #print('poss',boardcopy)
                boardcopy_hash = getHash(boardcopy)
                if player == 'p1':
                    value = 0 if p1states_value.get(boardcopy_hash) is None else p1states_value.get(boardcopy_hash)
                else:
                    value = 0 if p2states_value.get(boardcopy_hash) is None else p2states_value.get(boardcopy_hash)
                # print("value", value)
                if value >= value_max:
                    value_max = value
                    action = p
        #print("{} takes action {}".format(player, action))
        return action
    
    def getHash(matrix):
        matrixHash = str(matrix.reshape(9))
        return matrixHash
    
    def updateState(matrix, position, player):
        nonlocal playerSymbol
        if player == 'p1':
            playerSymbol = 'o'
            matrix[position] = 'x'
        else:
            playerSymbol = 'x'
            matrix[position] = 'o'
    
    while not isEnd:
        # Player 1
        
        positions = availablePositions(board)
        p1_action = chooseAction(positions, board, playerSymbol, 'p1')
        
        # take action and upate board state
        updateState(board, p1_action, 'p1')
        
        # check board status if it is end
        win = check_winner(board)
        if win is not None:
            break

        else:
            # Player 2
            print('You are player 2. You will use O')
            pos = int(input('Where do you want to place O? Insert a num val: '))
            pos = possible[pos-1]
            xx, xy = int(pos[0]), int(pos[1])
            board[xx][xy] = playerSymbol
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
tictactoe(1)

    