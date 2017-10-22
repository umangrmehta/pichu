#!/usr/bin/env python3
# Authors: Umang Mehta, Samanvitha Pradhan & Vaishnavi Srinivasan

import copy
import sys


def findPos(board, charToBeFound):
	return [(row, col) for col in range(0, 8, 1) for row in range(0, 8, 1) if board[row][col] == charToBeFound]


def updatePos(board, xPos1, yPos1, xPos2, yPos2, charToReplace, message):
	tempState = copy.deepcopy(board)
	tempState[xPos1][yPos1] = '.'
	tempState[xPos2][yPos2] = charToReplace
	# https://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
	flatList = [col for row in tempState for col in row]
	return flatList


def isEnemy(player, board, x,  y):
	if (player == "w" and board[x][y].islower()) or (player == "b" and board[x][y].isupper()):
		return True
	else:
		return False


def isFriend(player, board, x,  y):
	if (player == "w" and board[x][y].isupper()) or (player == "b" and board[x][y].islower()):
		return True
	else:
		return False


def piece(player, currPiece):
	if currPiece == 'pawn':
		pieceValue='P'
	if currPiece == 'bishop':
		pieceValue='B'
	if currPiece == 'queen':
		pieceValue='Q'
	if currPiece == 'king':
		pieceValue='K'
	if currPiece == 'rook':
		pieceValue='R'
	if currPiece == 'knight':
		pieceValue='N'
	if player == 'b':
		pieceValue = pieceValue.lower()
	return pieceValue


def onBoard(x, y):
	if 0 <= x <= 7 and  0 <= y <= 7:
		return True
	return False


def evaluation(board):
	if isTerminal(board):
		if firstPlayer == 'w':
			if ('K' in board) and not ('k' in board):
				turnCount = 55
			elif ('k' in board) and not ('K' in board):
				turnCount = -55
		elif firstPlayer == 'b':
			if ('k' in board) and not ('K' in board):
				turnCount = 55
			elif ('K' in board) and not ('k' in board):
				turnCount = -55
	else:
		whiteCount = 0
		blackCount = 0
		whiteCount += board.count('P') * 1
		whiteCount += board.count('R') * 7
		whiteCount += board.count('B') * float(3.5)
		whiteCount += board.count('N') * 4
		whiteCount += board.count('Q') * float(13.5)
		blackCount += board.count('p') * 1
		blackCount += board.count('r') * 7
		blackCount += board.count('b') * float(3.5)
		blackCount += board.count('n') * 4
		blackCount += board.count('q') * float(13.5)
		if firstPlayer == 'w':
			turnCount = whiteCount - blackCount
		if firstPlayer == 'b':
			turnCount = blackCount - whiteCount
	return turnCount


def isTerminal(board):
	# TODO: Check if the Board State is a Terminal State
	if "K" in board and "k" in board:
		return False
	return True


def successors(player, board):
	# https://stackoverflow.com/questions/6614891/turning-a-list-into-nested-lists-in-python
	currentState = [board[i:i + 8] for i in range(0, len(board), 8)]
	successor = []
	# successor = [row for row in successor if row != []]
	# each successor for pawn
	pawnPos = findPos(currentState, piece(player, 'pawn'))
	for possiblePositions in range(0, len(pawnPos), 1):
		rowCounter = pawnPos[possiblePositions][0]
		colCounter = pawnPos[possiblePositions][1]
		# move pawn down
		if player == 'w':
			if onBoard(rowCounter+1,colCounter):
				if isEnemy(player,currentState,rowCounter+1,colCounter) or not isFriend(player,currentState,rowCounter+1,colCounter):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+1, colCounter, piece(player,'pawn'), 'Pawn at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1+1)+' column '+str(colCounter+1)))
			if rowCounter == 1:
				if not isFriend(player,currentState,rowCounter+1,colCounter) and not isFriend(player,currentState,rowCounter+2,colCounter):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+2, colCounter, piece(player,'pawn'), 'Pawn at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+2+1)+' column '+str(colCounter+1)))
			# move pawn left diagonally
			if onBoard(rowCounter+1, colCounter-1):
				if isEnemy(player,currentState,rowCounter+1,colCounter-1):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+1, colCounter-1, piece(player,'pawn'), 'Pawn at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1+1)+' column '+str(colCounter-1+1)))
			# move pawn right diagonally
			if onBoard(rowCounter+1, colCounter+1):
				if isEnemy(player,currentState,rowCounter+1,colCounter+1):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+1, colCounter+1, piece(player,'pawn'), 'Pawn at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1+1)+' column '+str(colCounter+1+1)))
		# move pawn left
		if onBoard(rowCounter,colCounter-1):
			if isEnemy(player,currentState,rowCounter,colCounter-1) or not isFriend(player,currentState,rowCounter,colCounter-1):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, colCounter-1, piece(player,'pawn'), 'Pawn at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1)+' column '+str(colCounter-1+1)))
		# move pawn right
		if onBoard(rowCounter,colCounter+1):
			if isEnemy(player,currentState,rowCounter,colCounter+1) or not isFriend(player,currentState,rowCounter,colCounter+1):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, colCounter+1, piece(player,'pawn'), 'Pawn at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1)+' column '+str(colCounter+1+1)))
		if player == 'b':
			# move pawn up
			if onBoard(rowCounter-1, colCounter):
				if isEnemy(player, currentState, rowCounter-1, colCounter) or not isFriend(player, currentState, rowCounter-1, colCounter):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-1, colCounter, piece(player,'pawn'), 'Pawn at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-1+1)+' column '+str(colCounter+1)))
			if rowCounter == 6:
				if not isFriend(player,currentState,rowCounter-1,colCounter) and not isFriend(player,currentState,rowCounter-2,colCounter):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-2, colCounter, piece(player,'pawn'), 'Pawn at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-2+1)+' column '+str(colCounter+1)))
			# move pawn left diagonally
			if onBoard(colCounter-1,rowCounter-1) >= 0:
				if isEnemy(player,currentState,rowCounter-1,colCounter-1):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-1, colCounter-1, piece(player,'pawn'), 'Pawn at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-1+1)+' column '+str(colCounter-1+1)))
			# move pawn right diagonally
			if onBoard(colCounter+1,rowCounter-1):
				if isEnemy(player,currentState,rowCounter-1,colCounter+1):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-1, colCounter+1, piece(player,'pawn'), 'Pawn at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-1+1)+' column '+str(colCounter+1+1)))
	# each successor for rook
	rookPos = findPos(currentState, piece(player,'rook'))
	for possiblePositions in range(0, len(rookPos), 1):
		rowCounter = rookPos[possiblePositions][0]
		colCounter = rookPos[possiblePositions][1]
		# move rook up
		for i in range(rowCounter-1, -1, -1):
			if isFriend(player,currentState,i,colCounter):
				break
			elif isEnemy(player,currentState,i,colCounter):
				successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, piece(player,'rook'),'Rook at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(i+1)+' column '+str(colCounter+1)))
				break
			elif not isFriend(player,currentState,i,colCounter):
				successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, piece(player,'rook'),'Rook at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(i+1)+' column '+str(colCounter+1)))
			else:
				pass
		# move rook down
		for i in range(rowCounter+1, 8, 1):
			if isFriend(player,currentState,i,colCounter):
				break
			elif isEnemy(player,currentState,i,colCounter):
				successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, piece(player,'rook'),'Rook at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(i+1)+' column '+str(colCounter+1)))
				break
			elif not isEnemy(player,currentState,i,colCounter):
				successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, piece(player,'rook'),'Rook at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(i+1)+' column '+str(colCounter+1)))
			else:
				pass
		# move rook left
		for i in range(colCounter-1, -1, -1):
			if isFriend(player,currentState,rowCounter,i):
				break
			elif isEnemy(player,currentState,rowCounter,i):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, piece(player,'rook'),'Rook at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1)+' column '+str(i+1)))
				break
			elif not isFriend(player,currentState,rowCounter,i):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, piece(player,'rook'),'Rook at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1)+' column '+str(i+1)))
			else:
				pass
		# move rook right
		for i in range(colCounter+1, 8, 1):
			if isFriend(player,currentState,rowCounter,i):
				break
			elif isEnemy(player,currentState,rowCounter,i):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, piece(player,'rook'),'Rook at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1)+' column '+str(i+1)))
				break
			elif not isFriend(player,currentState,rowCounter,i):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, piece(player,'rook'),'Rook at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1)+' column '+str(i+1)))
			else:
				pass
	# each successor for bishop
	bishopPos = findPos(currentState, piece(player,'bishop'))
	for possiblePositions in range(0, len(bishopPos), 1):
		rowCounter = bishopPos[possiblePositions][0]
		colCounter = bishopPos[possiblePositions][1]
		# move bishop to the left
		for r in range(rowCounter, -1, -1):
			if onBoard(rowCounter-r,colCounter-r):
				if isFriend(player,currentState,rowCounter-r,colCounter-r):
					break
				elif isEnemy(player,currentState,rowCounter-r,colCounter-r):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-r, colCounter-r, piece(player,'bishop'),'Bishop at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-r+1)+' column '+str(colCounter-r+1)))
					break
				elif not isFriend(player,currentState,rowCounter-r,colCounter-r):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-r, colCounter-r, piece(player,'bishop'),'Bishop at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-r+1)+' column '+str(colCounter-r+1)))
				else:
					pass
		i = 1
		for r in range(rowCounter, 8, 1):
			if onBoard(rowCounter+i,colCounter+i):
				if isFriend(player,currentState,rowCounter+i,colCounter+i):
					break
				elif isEnemy(player,currentState,rowCounter+i,colCounter+i):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+i, colCounter+i, piece(player,'bishop'),'Bishop at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+i+1)+' column '+str(colCounter+i+1)))
					break
				elif not isFriend(player,currentState,rowCounter+i,colCounter+i):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+i, colCounter+i, piece(player,'bishop'),'Bishop at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+i+1)+' column '+str(colCounter+i+1)))
				else:
					pass
				i += 1
		i = 0
		# move bishop to the right
		for r in range(rowCounter, -1, -1):
			if onBoard(rowCounter-i,colCounter+i):
				if isFriend(player,currentState,rowCounter-i,colCounter+i):
					break
				elif isEnemy(player,currentState,rowCounter-i,colCounter+i):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-i, colCounter+i, piece(player,'bishop'),'Bishop at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-i+1)+' column '+str(colCounter+i+1)))
					break
				elif not isFriend(player,currentState,rowCounter-i,colCounter+i):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-i, colCounter+i, piece(player,'bishop'),'Bishop at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-i+1)+' column '+str(colCounter+i+1)))
				else:
					pass
				i += 1
		i = 1
		for r in range(rowCounter, 8, 1):
			if onBoard(rowCounter+i,colCounter-i):
				if isFriend(player,currentState,rowCounter+i,colCounter-i):
					break
				elif isEnemy(player,currentState,rowCounter+i,colCounter-i):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+i, colCounter-i, piece(player,'bishop'),'Bishop at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+i+1)+' column '+str(colCounter-i+1)))
					break
				elif not isFriend(player,currentState,rowCounter+i,colCounter-i):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+i, colCounter-i, piece(player,'bishop'),'Bishop at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+i+1)+' column '+str(colCounter-i+1)))
				else:
					pass
				i += 1
	# each successor for queen
	queenPos = findPos(currentState, piece(player,'queen'))
	for possiblePositions in range(0, len(queenPos), 1):
		rowCounter = queenPos[possiblePositions][0]
		colCounter = queenPos[possiblePositions][1]
		# move queen to the left
		for r in range(rowCounter, -1, -1):
			if onBoard(rowCounter-r,colCounter-r):
				if isFriend(player,currentState,rowCounter-r,colCounter-r):
					break
				elif isEnemy(player,currentState,rowCounter-r,colCounter-r):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-r, colCounter-r, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-r+1)+' column '+str(colCounter-r+1)))
					break
				elif not isFriend(player,currentState,rowCounter-r,colCounter-r):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-r, colCounter-r, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-r+1)+' column '+str(colCounter-r+1)))
				else:
					pass
		i = 1
		for r in range(rowCounter, 8, 1):
			if onBoard(rowCounter+i,colCounter+i):
				if isFriend(player,currentState,rowCounter+i,colCounter+i):
					break
				elif isEnemy(player,currentState,rowCounter+i,colCounter+i):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+i, colCounter+i, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+i+1)+' column '+str(colCounter+i+1)))
					break
				elif not isFriend(player,currentState,rowCounter+i,colCounter+i):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+i, colCounter+i, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+i+1)+' column '+str(colCounter+i+1)))
				else:
					pass
				i += 1
		i = 0
		# move queen to the right
		for r in range(rowCounter, -1, -1):
			if onBoard(rowCounter-i,colCounter+i):
				if isFriend(player,currentState,rowCounter-i,colCounter+i):
					break
				elif isEnemy(player,currentState,rowCounter-i,colCounter+i):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-i, colCounter+i, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-i+1)+' column '+str(colCounter+i+1)))
					break
				elif not isFriend(player,currentState,rowCounter-i,colCounter+i):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-i, colCounter+i, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-i+1)+' column '+str(colCounter+i+1)))
				else:
					pass
				i += 1
		i = 1
		for r in range(rowCounter, 8, 1):
			if onBoard(rowCounter+i,colCounter-i):
				if isFriend(player,currentState,rowCounter+i,colCounter-i):
					break
				elif isEnemy(player,currentState,rowCounter+i,colCounter-i):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+i, colCounter-i, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+i+1)+' column '+str(colCounter-i+1)))
					break
				elif not isFriend(player,currentState,rowCounter+i,colCounter-i):
					successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+i, colCounter-i, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+i+1)+' column '+str(colCounter-i+1)))
				else:
					pass
				i += 1
		# move queen up
		for i in range(rowCounter-1, -1, -1):
			if isFriend(player,currentState,i,colCounter):
				break
			elif isEnemy(player,currentState,i,colCounter):
				successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(i+1)+' column '+str(colCounter+1)))
				break
			elif not isFriend(player,currentState,i,colCounter):
				successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(i+1)+' column '+str(colCounter+1)))
			else:
				pass
		# move queen down
		for i in range(rowCounter+1, 8, 1):
			if isFriend(player, currentState, i, colCounter):
				break
			elif isEnemy(player, currentState, i, colCounter):
				successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(i+1)+' column '+str(colCounter+1)))
				break
			elif not isFriend(player, currentState, i, colCounter):
				successor.append(updatePos(currentState, rowCounter, colCounter, i, colCounter, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(i+1)+' column '+str(colCounter+1)))
			else:
				pass
		# move queen left
		for i in range(colCounter-1, -1, -1):
			if isFriend(player, currentState, rowCounter, i):
				break
			elif isEnemy(player, currentState, rowCounter, i):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1)+' column '+str(i+1)))
				break
			elif not isFriend(player, currentState, rowCounter, i):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1)+' column '+str(i+1)))
			else:
				pass
		# move queen right
		for i in range(colCounter+1, 8, 1):
			if isFriend(player, currentState, rowCounter, i):
				break
			elif isEnemy(player, currentState, rowCounter, i):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1)+' column '+str(i+1)))
				break
			elif not isFriend(player, currentState, rowCounter, i):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, i, piece(player,'queen'),'Queen at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1)+' column '+str(i+1)))
			else:
				pass
	# each successor for king
	kingPos = findPos(currentState, piece(player, 'king'))
	for possiblePositions in range(0, len(kingPos), 1):
		rowCounter = kingPos[possiblePositions][0]
		colCounter = kingPos[possiblePositions][1]
		# move king up
		if onBoard(rowCounter-1,colCounter):
			if isEnemy(player,currentState,rowCounter-1,colCounter) or not isFriend(player,currentState,rowCounter-1,colCounter):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-1, colCounter, piece(player,'king'),'King at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-1+1)+' column '+str(colCounter+1)))
		# move king down
		if onBoard(rowCounter+1,colCounter):
			if isEnemy(player,currentState,rowCounter+1,colCounter) or not isFriend(player,currentState,rowCounter+1,colCounter):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+1, colCounter, piece(player,'king'),'King at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1+1)+' column '+str(colCounter+1)))
		# move king left
		if onBoard(rowCounter,colCounter-1):
			if isEnemy(player,currentState,rowCounter,colCounter-1) or not isFriend(player,currentState,rowCounter,colCounter-1):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, colCounter-1, piece(player,'king'),'King at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1)+' column '+str(colCounter-1+1)))
		# move king right
		if onBoard(rowCounter,colCounter+1):
			if isEnemy(player,currentState,rowCounter,colCounter+1) or not isFriend(player,currentState,rowCounter,colCounter+1):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter, colCounter+1, piece(player,'king'),'King at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1)+' column '+str(colCounter+1+1)))
		# move king left diagonally down
		if onBoard(rowCounter+1,colCounter-1):
			if isEnemy(player,currentState,rowCounter+1,colCounter-1) or not isFriend(player,currentState,rowCounter+1,colCounter-1):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+1, colCounter-1, piece(player,'king'),'King at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-1+1)+' column '+str(colCounter-1+1)))
		# move king right diagonally down
		if onBoard(rowCounter+1,colCounter+1):
			if isEnemy(player,currentState,rowCounter+1,colCounter+1) or not isFriend(player,currentState,rowCounter+1,colCounter+1):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+1, colCounter+1, piece(player,'king'),'King at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1+1)+' column '+str(colCounter+1+1)))
		# move king left diagonally up
		if onBoard(rowCounter-1,colCounter-1):
			if isEnemy(player,currentState,rowCounter-1,colCounter-1) or not isFriend(player,currentState,rowCounter-1,colCounter-1):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-1, colCounter-1, piece(player,'king'),'King at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-1+1)+' column '+str(colCounter-1+1)))
		# move king right diagonally up
		if onBoard(rowCounter-1,colCounter+1):
			if isEnemy(player,currentState,rowCounter-1,colCounter+1) or not isFriend(player,currentState,rowCounter-1,colCounter+1):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-1, colCounter+1, piece(player,'king'),'King at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-1+1)+' column '+str(colCounter+1+1)))
	# each successor for knight
	knightPos = findPos(currentState, piece(player,'knight'))
	for possiblePositions in range(0, len(knightPos), 1):
		rowCounter = knightPos[possiblePositions][0]
		colCounter = knightPos[possiblePositions][1]
		# move knight up right L
		if onBoard(rowCounter-1,colCounter+2):
			if isEnemy(player,currentState,rowCounter-1,colCounter+2) or not isFriend(player,currentState,rowCounter-1,colCounter+2):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-1, colCounter+2, piece(player,'knight'),'Knight at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-1+1)+' column '+str(colCounter+1+2)))
		if onBoard(rowCounter-2,colCounter+1):
			if isEnemy(player,currentState,rowCounter-2,colCounter+1) or not isFriend(player,currentState,rowCounter-2,colCounter+1):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-2, colCounter+1, piece(player,'knight'),'Knight at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-2+1)+' column '+str(colCounter+1+1)))
		# move knight up left L
		if onBoard(rowCounter-1,colCounter-2):
			if isEnemy(player,currentState,rowCounter-1,colCounter-2) or not isFriend(player,currentState,rowCounter-1,colCounter-2):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-1, colCounter-2, piece(player,'knight'),'Knight at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-1+1)+' column '+str(colCounter+1-2)))
		if onBoard(rowCounter-2,colCounter+1):
			if isEnemy(player,currentState,rowCounter-2,colCounter-1) or not isFriend(player,currentState,rowCounter-2,colCounter-1):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter-2, colCounter-1, piece(player,'knight'),'Knight at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter-2+1)+' column '+str(colCounter+1+1)))
		# move knight down left L
		if onBoard(rowCounter+2,colCounter+1):
			if isEnemy(player,currentState,rowCounter+2,colCounter+1) or not isFriend(player,currentState,rowCounter+2,colCounter+1):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+2, colCounter+1, piece(player,'knight'),'Knight at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+2+1)+' column '+str(colCounter+1+1)))
		if onBoard(rowCounter+1,colCounter+2):
			if isEnemy(player,currentState,rowCounter+1,colCounter+2) or not isFriend(player,currentState,rowCounter+1,colCounter+2):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+1, colCounter+2, piece(player,'knight'),'Knight at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1+1)+' column '+str(colCounter+1+2)))
		# move knight down left L
		if onBoard(rowCounter+2,colCounter-1):
			if isEnemy(player,currentState,rowCounter+2,colCounter-1) or not isFriend(player,currentState,rowCounter+2,colCounter-1):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+2, colCounter-1, piece(player,'knight'),'Knight at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+2+1)+' column '+str(colCounter+1-1)))
		if onBoard(rowCounter+1,colCounter-2):
			if isEnemy(player,currentState,rowCounter+1,colCounter-2) or not isFriend(player,currentState,rowCounter+1,colCounter-2):
				successor.append(updatePos(currentState, rowCounter, colCounter, rowCounter+1, colCounter-2, piece(player,'knight'),'Knight at row '+str(rowCounter+1)+' column '+str(colCounter+1)+' to row '+str(rowCounter+1+1)+' column '+str(colCounter+1-2)))
	return successor


# TODO: Minimax with Alpha-Beta Pruning
def decision():
	# for s in successors(inputBoard):
	# 	print(s['board'])
	# 	print(min_value(s, -100, 100, 1))
	if not isTerminal(inputBoard):
		return max(successors(firstPlayer, inputBoard), key=lambda successor: minValue(successor, -100, 100, 1))
	else:
		if evaluation(inputBoard) > 0:
			return "You have already Won"
		else:
			return "You have already Lost"


def maxValue(board, alpha, beta, level):
	if isTerminal(board) or level == horizon:
		return evaluation(board)
	else:
		for successor in successors(firstPlayer, board):
			value = minValue(successor, alpha, beta, level + 1)
			if value > alpha:
				alpha = value
			if alpha >= beta:
				return alpha
		return alpha


def minValue(board, alpha, beta, level):
	if isTerminal(board) or level == horizon:
		return evaluation(board)
	else:
		for successor in successors(enemyPlayer, board):
			value = maxValue(successor, alpha, beta, level + 1)
			if value < beta:
				beta = value
			if alpha >= beta:
				return beta
		return beta


inputBoard = []
firstPlayer = str(sys.argv[1])
initialPosition = str(sys.argv[2])
timer = str(sys.argv[2])
# initialPosition = 'RNB.KBNRPP...P.....p...b....................q...ppp.ppp.rnbQk.nr'
if firstPlayer == "w":
	enemyPlayer = "b"
else:
	enemyPlayer = "w"

horizon = 3

for counter in range(0, len(initialPosition), 1):
	inputBoard.append(initialPosition[counter])

best_move = decision()
print("".join(best_move))
