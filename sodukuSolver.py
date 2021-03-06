# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 09:00:00 2021

@author: brendanlia
"""
import time

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def valid(board, num , row, col):
    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False
    boxX = col // 3
    boxY = row // 3
    for i in range(boxX*3, boxY*3+3):
        for j in range(boxY*3, boxX*3+3):
            if board[j][i] == num and (j,i) != (row, col):
                return False
    return True

def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(board, i, row, col):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

board = [
    [6,0,0,0,0,0,0,4,0],
    [1,8,0,0,0,3,5,0,0],
    [3,0,7,0,0,0,6,8,0],
    [7,0,8,0,0,0,0,6,0],
    [0,0,3,4,0,0,0,0,0],
    [0,0,0,0,5,2,0,3,0],
    [0,0,0,0,4,1,0,7,9],
    [0,0,0,3,2,0,0,0,0],
    [0,0,0,0,0,0,2,0,0]
]

printBoard(board)
t = time.time()
solve(board)
elapsed = time.time()-t
print('---------------------------------------------')
print('Solution')
printBoard(board)
print(str(elapsed) + 'sec')
















