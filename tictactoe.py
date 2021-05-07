# -*- coding: utf-8 -*-

"""
Created on Thu Apr 29 23:05:47 2021

@author: annie
"""
import numpy as np

def check_winner(matrix):  
    xpos = ''
    opos = ''
    
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
            elif j == 'o':
                xpos += '0'
                opos += '1'
            else:
               xpos += '0'
               opos += '1' 
    
    # convert to binary string
    xpos = xpos.encode('ascii')
    opos = opos.encode('ascii')

    for i in winnercombs:
        if i and xpos == i:
            print('Winner is X')
            return True
        elif i and opos == i:
            print('Winner is O')
            return True
    
    return False
            

def tictactoe(players):
    assert(players <= 2)
    assert(players > 0)
    
    board = np.zeros((3,3), dtype=str)
    
    if players == 1:
        single_player(board)
    
    if players == 2:
        two_player(board)
        
def single_player(board):
    return

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
            pos = int(input('Where do you want to place X? Insert a num val: '))
            pos = possible[pos-1]
            xx, xy = int(pos[0]), int(pos[1])
            board[xx][xy] = turn
            turn = 'x'
            #check_winner(board)
            
def single_player_bad_ai(board):
    return
    
#two player tic tac toe simulation
tictactoe(2)

    