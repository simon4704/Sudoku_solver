# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:06:20 2021

@author: simon
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:20:44 2021

@author: simon

Version 1.2 with improved AI :3 lol
This version starts by checking what values can be in each position before
starting the bruteforce


Saves around 1-1.5 seconds
"""

import numpy as np
import matplotlib.pyplot as plt
import time

t0 = time.time()

#%%

# plt.plot(1,2, 'ro')
# plt.show()
# plt.plot((3),(4), 'bo')

#%%

board = np.array([[0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0]])



board = np.array([[0,0,0,1,0,6,2,0,4],
                  [0,4,0,0,0,0,0,5,0],
                  [1,0,0,7,0,0,0,0,0],
                  [0,0,0,0,5,0,0,3,0],
                  [0,0,0,0,0,3,0,0,0],
                  [0,0,1,0,0,0,6,7,2],
                  [6,9,2,0,0,0,0,0,5],
                  [0,0,0,4,0,0,0,0,0],
                  [0,3,0,0,6,0,0,0,8]])

board = np.zeros([9,9]).astype(int)

board = np.array([[8,0,0,0,0,0,0,0,0],
                  [0,0,3,6,0,0,0,0,0],
                  [0,7,0,0,9,0,2,0,0],
                  [0,5,0,0,0,7,0,0,0],
                  [0,0,0,0,4,5,7,0,0],
                  [0,0,0,1,0,0,0,3,0],
                  [0,0,1,0,0,0,0,6,8],
                  [0,0,8,5,0,0,0,1,0],
                  [0,9,0,0,0,0,4,0,0]])

board = np.array([[9,0,0,5,6,0,4,0,0],
                  [0,0,0,0,0,1,0,6,0],
                  [0,5,0,0,0,2,0,0,0],
                  [4,0,0,0,0,0,0,0,7],
                  [0,9,0,3,8,0,0,2,0],
                  [0,0,0,0,0,5,0,0,0],
                  [0,0,8,0,0,0,2,0,0],
                  [0,0,0,0,1,0,0,0,0],
                  [0,3,0,6,9,0,0,8,0]])

preDefined = np.sign(board)

cp = [0,0] # cp = currentPosition
currentValue = 0


#%%

def IncreaseCP():
    if cp[1] < 8:
        cp[1] += 1
    else:
        cp[1] = 0
        cp[0] += 1

def DecreaseCP():
    if cp[1] > 0:
        cp[1] -= 1
    else:
        cp[1] = 8
        cp[0] -= 1




def RoundToCell(pos):
    cellCenter = [0,0]
    for i in range(2):
        if pos[i] < 3:
            cellCenter[i] = 1
        elif pos[i] < 6:
            cellCenter[i] = 4
        elif pos[i] < 9:
            cellCenter[i] = 7
    
    return cellCenter


def CheckAllowed(pos): # pos=position
    row = board[pos[0],:]
    col = board[:,pos[1]]
    
    cc = RoundToCell(pos) # cc = cellCenter
    cell = board[cc[0]-1:cc[0]+2, cc[1]-1:cc[1]+2]
    
    if np.any(row == currentValue) or np.any(col == currentValue) or np.any(cell == currentValue):
        return False
    else:
        return True

#%%

candidates = np.zeros([9,9,9]).astype(int) # the numbers that are allowed in this position
candidateIndex = (-1)*np.ones([9,9]).astype(int) # index for the number we are currently testing for in the bruteforce part

for i in range(9):
    for j in range(9):
        allNums = np.arange(1,10)
        row = board[i,:]
        col = board[:,j]
        cc = RoundToCell([i,j])
        cell = board[cc[0]-1:cc[0]+2, cc[1]-1:cc[1]+2]
        
        for value in row:
            if np.any(allNums == value):
                allNums = np.delete(allNums, np.argwhere(allNums==value))
        
        for value in row:
            if np.any(allNums == value):
                allNums = np.delete(allNums, np.argwhere(allNums==value))
        
        for row in cell:
            for value in row:
                if np.any(allNums == value):
                    allNums = np.delete(allNums, np.argwhere(allNums==value))       

        for candidate in allNums:
            candidates[i,j,candidate-1] = candidate

ni = 0

nt = 0

while True:
    ni += 1
    # print()
    # print("ni={}".format(ni))
    # print(board)
    if preDefined[cp[0], cp[1]] == 0:
        currentValue = board[cp[0], cp[1]]
        
        # print(currentValue)
        while True:
            # print(cp)
            if currentValue < 9 and candidateIndex[cp[0], cp[1]] < 8:
                
                candidateIndex[cp[0], cp[1]] += 1
                
                # print(currentValue)
                
                # print(candidateIndex[cp[0], cp[1]])
                
                # print(candidates[cp[0], cp[1], candidateIndex[cp[0],cp[1]]])
                
                currentValue = candidates[cp[0], cp[1], candidateIndex[cp[0], cp[1]]]
                
                
                
                while candidates[cp[0], cp[1], candidateIndex[cp[0],cp[1]]] == 0 and candidateIndex[cp[0], cp[1]] < 8:
                    candidateIndex[cp[0], cp[1]] += 1
                currentValue = candidates[cp[0], cp[1], candidateIndex[cp[0],cp[1]]]
                
                # print(currentValue)
            else:
                board[cp[0], cp[1]] = 0
                candidateIndex[cp[0], cp[1]] = -1
                DecreaseCP()
                while preDefined[cp[0], cp[1]] == 1:
                    DecreaseCP()                    
                break
            
            allowed = CheckAllowed(cp)
            if allowed == True:
                # print("allowed")
                board[cp[0], cp[1]] = currentValue
                IncreaseCP()
                break
            
            if allowed == False and currentValue == 9:
                board[cp[0], cp[1]] = 0
                candidateIndex[cp[0], cp[1]] = -1
                DecreaseCP()
                while preDefined[cp[0], cp[1]] == 1:
                    DecreaseCP()                    
                break
            
            
        if cp[0] == 9:
            break
    
    else:
        IncreaseCP()
        if cp[0] == 9:
            break


t1 = time.time()


print(t1-t0)

print(board)
print(ni)


