#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 14:25:04 2021

@author: annie
"""
import numpy as np
import pickle

states = []
p1states = []
p2states = []
lr = 0.2
exp_rate = 0.3
decay_gamma = 0.9
states_value = {}
p1states_value = {}
p2states_value = {}
playerSymbol = 1


#print(check_winner([['x','x','x'],['','',''],['','','']]))

def play(rounds=100):
    board = np.zeros((3,3), dtype=str)
    playerSymbol = 'x'
    isEnd = False
    
    def check_winner(matrix): 
        nonlocal isEnd
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
                    opos += '1' 
    
        # convert to binary string
        xpos = xpos.encode('ascii')
        opos = opos.encode('ascii')
        allpos = allpos.encode('ascii')

        for i in winnercombs:
            if i and xpos == i:
                isEnd=True
                print('Winner is X')
                return 1
            elif i and opos == i:
                isEnd=True
                print('Winner is O')
                return -1
    
        if allpos == b'111111111':
            isEnd=True
            print('Board is full')
            return 'full'
        
        return None
    
    def availablePositions(matrix):
        position = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    position.append((i,j))
        print(position)
        return position
    
    def getHash(matrix):
        matrixHash = str(matrix.reshape(9))
        return matrixHash
    
    def chooseAction(positions, current_board, symbol, player):
        exp_rate = 0.3
        print('current',current_board)
        if np.random.uniform(0, 1) <= exp_rate:
            # take random action
            idx = np.random.choice(len(positions))
            action = positions[idx]
        else:
            value_max = -999
            action = positions[0]
            for p in positions:
                print(p)
                boardcopy = current_board.copy()
                boardcopy[p] = playerSymbol
                print('poss',boardcopy)
                boardcopy_hash = getHash(boardcopy)
                if player == 'p1':
                    value = 0 if states_value.get(boardcopy_hash) is None else states_value.get(boardcopy_hash)
                else:
                    value = 0 if states_value.get(boardcopy_hash) is None else states_value.get(boardcopy_hash)
                # print("value", value)
                if value >= value_max:
                    value_max = value
                    action = p
        print("{} takes action {}".format(player, action))
        return action
    
    def updateState(matrix, position, player):
        nonlocal playerSymbol
        if player == 'p1':
            playerSymbol = 'o'
            matrix[position] = 'x'
        else:
            playerSymbol = 'x'
            matrix[position] = 'o'
    
    def feedReward(reward, player):
        if player == 'p1':
            for st in reversed(p1states):
                if p1states_value.get(st) is None:
                    p1states_value[st] = 0
                p1states_value[st] += lr*(decay_gamma*reward - p1states_value[st])
                reward = p1states_value[st]
        else:
            for st in reversed(p2states):
                if p2states_value.get(st) is None:
                    p2states_value[st] = 0
                p2states_value[st] += lr*(decay_gamma*reward - p2states_value[st])
                reward = p2states_value[st]
    
    def giveReward(matrix):
        result = check_winner(matrix)
        if result == 1:
            feedReward(1,'p1')
            feedReward(0,'p2')
        elif result == -1:
            feedReward(0,'p1')
            feedReward(1,'p2')
        else:
            feedReward(0.1,'p1')
            feedReward(0.5,'p2')
    
    def addState(state, player):
        if player == 'p1':
            p1states.append(state)
        else:
           p2states.append(state)
    """
    def reset():
        nonlocal p1states
        nonlocal p2states
        nonlocal states
        states = []
        p1states = []
        p1states = []
    """
        
    for i in range(rounds):
        if i%1000 == 0:
            print("Rounds {}".format(i))
        p1states = []
        p1states = []
        while not isEnd:
            # Player 1
            positions = availablePositions(board)
            p1_action = chooseAction(positions, board, playerSymbol,'p1')
            # take action and upate board state
            updateState(board, p1_action,'p1')
            board_hash = getHash(board)
            addState(board_hash,'p1')
            # check board status if it is end

            win = check_winner(board)
            if win is not None:
                # self.showBoard()
                # ended with p1 either win or draw
                giveReward(board)
                board = np.zeros((3,3), dtype=str)
                break

            else:
                # Player 2
                positions = availablePositions(board)
                p2_action = chooseAction(positions, board, playerSymbol,'p2')
                updateState(board,p2_action,'p2')
                board_hash = getHash(board)
                addState(board_hash, 'p2')
                
                win = check_winner(board)
                if win is not None:
                    # self.showBoard()
                    # ended with p2 either win or draw
                    giveReward(board)
                    board = np.zeros((3,3), dtype=str)
                    break


play(1)
