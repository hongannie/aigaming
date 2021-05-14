
import numpy as np
import pickle

lr = 0.2
decay_gamma = 0.9
p1states_value = {}
p2states_value = {}

def play(rounds=100):
    
    #variables
    board = np.zeros((3,3), dtype=str)
    symbol = 'x'
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
        #print(matrix)
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
                isEnd=True
                print('Winner is X!')
                return 1
            elif i and opos == i:
                isEnd=True
                print('Winner is O!')
                return -1
    
        if allpos == b'111111111':
            isEnd=True
            print("It's a draw!")
            return 'draw'
        
        return None
    
    # checks for all empty positions
    def availablePlays(matrix):
        position = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    position.append((i,j))
        return position
    
    def getHash(matrix):
        matrixHash = str(matrix.reshape(9))
        return matrixHash
    
    def chooseAction(positions, current_board, symbol, player):
        exploration_rate = 0.3
        # make a random move
        if np.random.uniform(0, 1) <= exploration_rate:
            pos = np.random.choice(len(positions))
            action = positions[pos]
        else:
            value_max = -999
            action = positions[0]
            #iterate through all possible positions
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
    
    def updateState(matrix, position, player):
        nonlocal symbol
        if player == 'p1':
            symbol = 'o'
            matrix[position] = 'x'
        else:
            symbol = 'x'
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
            feedReward(0.5,'p1')
            feedReward(0.5,'p2')
    
    def addState(state, player):
        if player == 'p1':
            p1states.append(state)
        else:
           p2states.append(state)
        
    for i in range(rounds):
        print('game',i)
        if i%100 == 0:
            print("Rounds", i)
        p1states = p2states = []
        board = np.zeros((3,3), dtype=str)
        
        while not isEnd:
            #player 1
            positions = availablePlays(board)
            p1_action = chooseAction(positions, board, symbol,'p1')
            updateState(board, p1_action,'p1')
            board_hash = getHash(board)
            addState(board_hash,'p1')

            win = check_winner(board)
            if win is not None:
                giveReward(board)
                isEnd = False
                break

            else:
                #player 2
                positions = availablePlays(board)
                p2_action = chooseAction(positions, board, symbol,'p2')
                updateState(board,p2_action,'p2')
                board_hash = getHash(board)
                addState(board_hash, 'p2')
                
                win = check_winner(board)
                if win is not None:
                    giveReward(board)
                    isEnd = False
                    break


play(50)
print(p1states_value)

fw = open('policy_' + 'p1', 'wb')
pickle.dump(p1states_value, fw)
fw.close()

fw = open('policy_' + 'p2', 'wb')
pickle.dump(p2states_value, fw)
fw.close()

